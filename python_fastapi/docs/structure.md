# FastAPI sample structure

> This structure is insprired by many frameworks:
>
> - FastAPI
> - Vue.js

## Basic Structure

This project contains some important parts:

- `Configuration`
- `Source files`
- `Storage` for volumes
- `Test files`

Structure tree:

```bash

```

### Configuration

The configuration will be placed in `./config`, this is where you can probabily store all config for the components.

### Tests file

Test files are placed in `./tests/` folder. In this core, I prefer to use `pytest` package. All the tests in folder `tests/` can be run in one simple command:

```bash
pytest tests/
```

Just remember test file in `tests` must follows these patterns `test_name.py` or `name_test.py`

### Source files

Inspired by `Vue` structure

### Storage

All mounted resources should be put in `./storage/`. Some resources could be placed here:

- Model **weights**
- API Credential key
- Log files
