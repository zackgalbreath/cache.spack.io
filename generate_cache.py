#!/usr/bin/env python3

# This script will generate package metadata files for
# each package in the latest version of spack
#
# Usage:
# python generate_cache.py


import json
import yaml
import sys
import os
import requests

import spack.database
import spack.repo
import spack.spec

here = os.getcwd()

CACHE = "https://cache.e4s.io/build_cache/index.json"
db_root = os.path.join(here, "spack-db")


def write_json(content, filename):
    with open(filename, "w") as outfile:
        outfile.write(json.dumps(content, indent=4))


# Template for cache data
template = """---
title: "%s"
layout: cache
category: package
meta: %s
spec_files: 
 - %s
---"""


def main():

    response = requests.get(CACHE)
    if response.status_code != 200:
        sys.exit("Issue with request to get package index: %s" % response.reason)
    index = response.json()

    # Write index.json to file
    if not os.path.exists(db_root):
        os.makedirs(db_root)
    write_json(index, os.path.join(db_root, "index.json"))

    # yeah this is awkward <--- from @tgamblin :D
    db = spack.database.Database(None, db_root)

    # Organize specs by package
    specs = {}

    # keep lookup of specs
    with db.read_transaction():
        packages = sorted(set(rec.spec.name for rec in db._data.values()))
        for record in db._data.values():
            specs.setdefault(record.spec.name, []).append(record.spec)

    # We will save a metadata file
    count = 0
    meta = {
        "version": index["database"]["version"],
        "count": len(index["database"]["installs"]),
    }
    del index

    # For funsies store top level metrics
    parameters = {}
    compilers = {}
    arches = {"platform": {}, "platform_os": {}, "compiler": {}, "target": {}}
    count = 0

    # For each package, generate a data page, including the spec.json
    for package_name, speclist in specs.items():
        for s in speclist:
            count += 1
            nodes = s.to_dict()["spec"]["nodes"]
            for spec in nodes:
                for paramname, setting in spec["parameters"].items():

                    # Is true or not empty list
                    if setting:
                        if paramname not in parameters:
                            parameters[paramname] = 0
                        parameters[paramname] += 1

                for key, value in spec["arch"].items():

                    # Target can have another level of nesting
                    if key == "target" and isinstance(value, dict):
                        value = "%s %s" % (value["vendor"], value["name"])
                    if value not in arches[key]:
                        arches[key][value] = 0
                    arches[key][value] += 1

                compiler = "%s@%s" % (
                    spec["compiler"]["name"],
                    spec["compiler"]["version"],
                )
                if compiler not in compilers:
                    compilers[compiler] = 0
                compilers[compiler] += 1

    # For each meta, write to data file
    meta_file = os.path.join(here, "_data", "meta.yaml")
    meta["compilers"] = compilers
    meta["parameters"] = parameters
    meta["compiler_count"] = len(compilers)
    meta["count"] = count
    with open(meta_file, "w") as fd:
        fd.write(yaml.dump(meta_file))

    # For each spec, write to the _cache folder
    for package_name, speclist in specs.items():

        # Keep a set of summary metrics for a spec
        metrics = {"versions": set(), "compilers": set()}

        package_dir = os.path.join(here, "_cache", package_name)
        if not os.path.exists(package_dir):
            os.makedirs(package_dir)
        spec_files = []
        for i, spec in enumerate(speclist):
            metrics["versions"].add(str(spec.version))
            metrics["compilers"].add(str(spec.compiler))
            spec_name = "spec-%s.json" % i
            spec_file = os.path.join(package_dir, spec_name)
            write_json(spec.to_dict(), spec_file)
            spec_files.append('"%s": %s' % (str(spec), spec_name))
        metrics["versions"] = list(metrics["versions"])
        metrics["compilers"] = list(metrics["compilers"])
        render = template % (
            package_name,
            json.dumps(metrics),
            " - ".join([x + "\n" for x in spec_files]),
        )
        md_file = os.path.join(package_dir, "index.md")
        with open(md_file, "w") as fd:
            fd.write(render)


if __name__ == "__main__":
    main()
