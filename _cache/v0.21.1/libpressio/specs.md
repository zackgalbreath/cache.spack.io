---
title: "libpressio"
layout: cache
categories: [package, v0.21.1]
meta: {"versions": ["0.95.1"], "compilers": ["cce@=15.0.1", "gcc@=11.4.0", "oneapi@=2023.2.0"], "oss": ["rhel8", "ubuntu20.04"], "platforms": ["linux"], "targets": ["x86_64_v3", "zen4"], "stacks": ["e4s", "e4s-cray-rhel", "e4s-oneapi", "root"], "num_specs": 5, "num_specs_by_stack": {"root": 5, "e4s-cray-rhel": 1, "e4s": 3, "e4s-oneapi": 1}}
spec_details: [{"hash": "6qs7pdryxsjl7q5o3fmes7dtorrcah43", "compiler": "cce@=15.0.1", "versions": ["0.95.1"], "os": "rhel8", "platform": "linux", "target": "zen4", "variants": ["~arc", "+bitgrooming", "~blosc", "~boost", "build_system=cmake", "build_type=Release", "+bzip2", "+core", "~cuda", "~cusz", "~digitrounding", "~docs", "+fpzip", "~ftk", "generator=make", "+hdf5", "~ipo", "+json", "+libdistributed", "+lua", "~magick", "+mgard", "~mgardx", "+mpi", "~ndzip", "+netcdf", "+openmp", "~petsc", "+python", "~qoz", "+remote", "+sz", "+sz3", "~szauto", "+unix", "+zfp"], "stacks": ["root", "e4s-cray-rhel"], "size": "-", "tarball": "https://binaries.spack.io/v0.21.1/build_cache/linux-rhel8-zen4/cce-15.0.1/libpressio-0.95.1/linux-rhel8-zen4-cce-15.0.1-libpressio-0.95.1-6qs7pdryxsjl7q5o3fmes7dtorrcah43.spack"}, {"hash": "2nm2doazk2l7xpxjflcyb6g5phcqf47v", "compiler": "gcc@=11.4.0", "versions": ["0.95.1"], "os": "ubuntu20.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~arc", "+bitgrooming", "~blosc", "~boost", "build_system=cmake", "build_type=Release", "+bzip2", "+core", "+cuda", "cuda_arch=80", "+cusz", "~digitrounding", "~docs", "+fpzip", "~ftk", "generator=make", "+hdf5", "~ipo", "+json", "+libdistributed", "+lua", "~magick", "+mgard", "~mgardx", "+mpi", "~ndzip", "+netcdf", "+openmp", "~petsc", "+python", "~qoz", "+remote", "+sz", "+sz3", "~szauto", "+unix", "+zfp"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/v0.21.1/build_cache/linux-ubuntu20.04-x86_64_v3/gcc-11.4.0/libpressio-0.95.1/linux-ubuntu20.04-x86_64_v3-gcc-11.4.0-libpressio-0.95.1-2nm2doazk2l7xpxjflcyb6g5phcqf47v.spack"}, {"hash": "c4qmldnuip2gsmb2os652anj7kretlxz", "compiler": "gcc@=11.4.0", "versions": ["0.95.1"], "os": "ubuntu20.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~arc", "+bitgrooming", "~blosc", "~boost", "build_system=cmake", "build_type=Release", "+bzip2", "+core", "~cuda", "~cusz", "~digitrounding", "~docs", "+fpzip", "~ftk", "generator=make", "+hdf5", "~ipo", "~json", "+libdistributed", "+lua", "~magick", "~mgard", "~mgardx", "+mpi", "~ndzip", "~netcdf", "+openmp", "~petsc", "+python", "~qoz", "~remote", "+sz", "+sz3", "~szauto", "+unix", "+zfp"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/v0.21.1/build_cache/linux-ubuntu20.04-x86_64_v3/gcc-11.4.0/libpressio-0.95.1/linux-ubuntu20.04-x86_64_v3-gcc-11.4.0-libpressio-0.95.1-c4qmldnuip2gsmb2os652anj7kretlxz.spack"}, {"hash": "te5i2guggc6tzv5y7z74uja5wkliplig", "compiler": "gcc@=11.4.0", "versions": ["0.95.1"], "os": "ubuntu20.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~arc", "+bitgrooming", "~blosc", "~boost", "build_system=cmake", "build_type=Release", "+bzip2", "+core", "+cuda", "cuda_arch=90", "+cusz", "~digitrounding", "~docs", "+fpzip", "~ftk", "generator=make", "+hdf5", "~ipo", "+json", "+libdistributed", "+lua", "~magick", "+mgard", "~mgardx", "+mpi", "~ndzip", "+netcdf", "+openmp", "~petsc", "+python", "~qoz", "+remote", "+sz", "+sz3", "~szauto", "+unix", "+zfp"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/v0.21.1/build_cache/linux-ubuntu20.04-x86_64_v3/gcc-11.4.0/libpressio-0.95.1/linux-ubuntu20.04-x86_64_v3-gcc-11.4.0-libpressio-0.95.1-te5i2guggc6tzv5y7z74uja5wkliplig.spack"}, {"hash": "ns6du2i6xn5rvja3ozypsxmfpwf22asu", "compiler": "oneapi@=2023.2.0", "versions": ["0.95.1"], "os": "ubuntu20.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~arc", "+bitgrooming", "~blosc", "~boost", "build_system=cmake", "build_type=Release", "+bzip2", "+core", "~cuda", "~cusz", "~digitrounding", "~docs", "+fpzip", "~ftk", "generator=make", "+hdf5", "~ipo", "~json", "+libdistributed", "+lua", "~magick", "~mgard", "~mgardx", "+mpi", "~ndzip", "~netcdf", "+openmp", "~petsc", "+python", "~qoz", "~remote", "+sz", "+sz3", "~szauto", "+unix", "+zfp"], "stacks": ["e4s-oneapi", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.21.1/build_cache/linux-ubuntu20.04-x86_64_v3/oneapi-2023.2.0/libpressio-0.95.1/linux-ubuntu20.04-x86_64_v3-oneapi-2023.2.0-libpressio-0.95.1-ns6du2i6xn5rvja3ozypsxmfpwf22asu.spack"}]
---