# Revenue Variance Lens

Explains synthetic revenue variance by segment.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m revenue_variance_lens.cli --input data/sample_segments.json
```

## Test

```bash
python3 -m unittest discover tests
```
