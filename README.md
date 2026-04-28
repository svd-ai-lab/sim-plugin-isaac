# sim-plugin-isaac

Isaac driver for [sim-cli](https://github.com/svd-ai-lab/sim-cli),
distributed as an out-of-tree plugin.

Isaac Sim driver for sim (v1: one-shot subprocess).

## Install

```bash
sim plugin install isaac
```

Other paths:

```bash
pip install git+https://github.com/svd-ai-lab/sim-plugin-isaac@v0.1.0
pip install https://github.com/svd-ai-lab/sim-plugin-isaac/releases/download/v0.1.0/sim_plugin_isaac-0.1.0-py3-none-any.whl
pip install -e .
```

After install:

```bash
sim plugin doctor isaac
sim plugin sync-skills
```

## Development

```bash
git clone https://github.com/svd-ai-lab/sim-plugin-isaac
cd sim-plugin-isaac
uv sync
uv run pytest
```

## License

Apache-2.0.
