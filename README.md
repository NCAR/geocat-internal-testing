# GeoCAT Internal Testing

A place to share and demonstrate testing we're doing in GeoCAT. This repo is for contributors to GeoCAT. The differences between `geocat-internal-testing` and `geocat-scratch` are:

- this repository is specifically for testing, though what counts as testing can be broad, and
- the contents of this repo should, to the best of your ability, be reproducible.

## How to use this repository

1. Clone the repository to your local:

    ``` bash
    git clone https://github.com/NCAR/geocat-internal-testing
    ```

1. Make yourself a branch to work on:

    ``` bash
    git checkout -b my-branch
    ```

1. Find or create the relevant subdirectory. For example, if your testing relates to `geocat-viz`, find or create a top level folder named `geocat-viz`. Then, create a subdirectory named something specific to the testing you're creating, such as `contourf`. All of the scripts, notebooks, and other files you create should be placed in this subdirectory.

1. In your subdirectory, create a file named `README.md` and  describe the contents of the directory and the testing you're doing.

1. Also create a minimal environment file called `environment.yml` that can run the notebooks in the directory. Make sure to update this file with all additional dependencies you might add during the development of your notebooks.

### Testing Feature Development

If you are working on a feature in one of the GeoCAT repositories simultaneously, you may find it helpful to install that package from your development branch in your environment file. To do this, add the following to your environment file:

``` yaml
pip:
    - git+<link to github repo>@<branch>
```

Every time you push to that development branch, you can update your environment to use those changes by:

``` bash
conda env update -f environment.yml
```

Afterwards, be sure to restart your kernel.

## Contributing your changes

After you're done making your notebooks, you can add them to `main`.

Make a PR and merge it to main yourself. This will probably be changed in the future when this repo is more mature, but for now needing reviews is not very meaningful to the content that will be made here.
