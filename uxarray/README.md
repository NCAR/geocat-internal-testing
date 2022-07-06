# Uxarray Testing

## Contents

``` bash
(base) anissaz@cisl-pinestone uxarray % tree -P "*.ipynb"
.
├── data
├── initial-release
│   ├── uxarray-IO.ipynb
│   └── uxarray-release.ipynb
├── integrate
│   └── uxarray-integration-function.ipynb
└── performance
    ├── uxarray-performance.ipynb
    └── uxarray-super-computer.ipynb
```

### `./data/`: Data

Data shared by notebooks in this directory.

### `uxarray-pip.yml`
Generic environment file for building from a specific branch of the `uxarray` repository.

### `uxarray-release-testing.yml`
Generic environment file for building from a package installed on a private conda channel.

### `./initial-release/`: Initial Release Testing

Testing done ahead of the initial release of Uxarray, which mostly contained IO functionality.

### `./integrate/`: Integrate Function Testing

Testing done on the first function of uxarray, integrate. Mostly focused on performance improvements for the function.

### `./performance/`: Performance Testing

General performance testing of uxarray.
