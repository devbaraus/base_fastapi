# app


Start a project with:

```bash
docker-compose -f docker-compose.yml --project-directory . up
```

If you want to develop in docker with autoreload, use this command:

```bash
docker-compose -f docker-compose.yml -f docker-compose.dev.yml --project-directory . up
```

This command exposes application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f docker-compose.yml --project-directory . build
```


## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

## Migrations

If you want to migrate your database, you should run following commands:
```bash
# To run all migrations untill the migration with revision_id.
alembic upgrade "<revision_id>"

# To perform all pending migrations.
alembic upgrade "head"
```

### Reverting migrations

If you want to revert migrations, you should run:
```bash
# revert all migrations up to: revision_id.
alembic downgrade <revision_id>

# Revert everything.
 alembic downgrade base
```

### Migration generation

To generate migrations you should run:
```bash
# For automatic change detection.
alembic revision --autogenerate

# For empty file generation.
alembic revision
```
