# kubectl-stash

`kubectl-stash` is a command-line interface (CLI) tool designed to simplify the management of Kubernetes contexts and namespaces. By "stashing" frequently used configurations, `kubectl-stash` allows users to quickly switch between different Kubernetes environments without the need to repeatedly input common parameters.

## Features

- Interactive selection of Kubernetes contexts and namespaces.
- Stashing of environment, context, and namespace for quick reuse.
- Support for local and global configuration files to enhance flexibility in various working environments.

## Installation

To install `kubectl-stash`, navigate to the root directory of the cloned repository and run the following command:

```bash
python setup.py install
```

This will install `kubectl-stash` and its dependencies.

## Usage

You can use `kubectl-stash` by running the `kstash` command followed by optional flags to specify the namespace, context, and environment directly.

### Basic Command Structure

```bash
kstash -n <namespace> -c <context name> -e <environment>
```

### Interactive Mode

If you run `kstash` without any arguments, it will prompt you interactively to select or input the necessary parameters:

```bash
kstash
```

### List of Options

- `-n, --namespace`: Specify the Kubernetes namespace.
- `-c, --context`: Specify the Kubernetes context.
- `-e, --environment`: Specify the environment name.

For additional help and options, use:

```bash
kstash --help
```

## Configuration

`kubectl-stash` automatically manages configurations and stores them in a `.kubestash` file located in the user's home directory or the current working directory, depending on which is found first.

## Contributing

Contributions to `kubectl-stash` are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push to your branch.
5. Submit a pull request.

Please ensure your code adheres to the project's coding standards and include tests for new features or fixes.

## License

`kubectl-stash` is open-sourced software licensed under the [MIT license](LICENSE).

## Acknowledgments

- Kubernetes community for the inspiration.
- Contributors and supporters of the `kubectl-stash` project.

For more information, questions, or feedback, please contact the project maintainers.