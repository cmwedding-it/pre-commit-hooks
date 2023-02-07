custom pre-commit-hooks
================

### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/cmwedding-it/pre-commit-hooks
    rev: 1.0.0  # Use the ref you want to point at
    hooks:
     -   id: # ...
```

### Hooks available

#### `set-module-version`
sets odoo module version to `<commit-id>@<branch>`
