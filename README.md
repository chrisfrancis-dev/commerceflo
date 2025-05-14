### Commerceflo

Saas platform

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:
Setup and install ERPNext before installing commerceflo

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app git@github.com:chrisfrancis-dev/commerceflo.git
bench install-app commerceflo
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/commerceflo
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
