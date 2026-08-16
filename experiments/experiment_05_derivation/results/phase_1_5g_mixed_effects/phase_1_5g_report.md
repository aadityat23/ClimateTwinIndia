# ClimateTwin Phase 1.5G — Mixed-Effects Robustness

## Purpose

This analysis re-evaluates the frozen Phase 1.5 endpoints using a
binomial generalized linear mixed model with a question-level random
intercept.

No model inference or benchmark generation was performed.

## Primary endpoint

Baseline -> toward-GT alpha=0.99

- N pairs: 245
- Baseline propagation: 56.326531%
- Toward propagation: 68.979592%
- Difference: +12.6531 pp
- Exact McNemar p: 0.0026537861
- Mixed-model OR: 1.838698
- Mixed-model 95% interval:
  [1.384961,
   2.441086]
- Posterior P(beta > 0):
  0.999987

Question random-intercept SD:
0.736829

## Directional control

Away-GT alpha=0.99 -> toward-GT alpha=0.99

- N pairs: 245
- Away propagation: 41.224490%
- Toward propagation: 68.979592%
- Difference: +27.7551 pp
- Exact McNemar p: 3.7651773e-11
- Mixed-model OR: 3.843138
- Mixed-model 95% interval:
  [2.877542,
   5.132751]
- Posterior P(beta > 0):
  1.000000

Question random-intercept SD:
0.910654

## Interpretation

The mixed-effects model is a robustness analysis addressing repeated
observations associated with the same benchmark question.

The original paired McNemar tests remain the frozen Phase 1.5 primary
analysis. This model does not replace them.

The result should be interpreted as evidence about directional
sensitivity of deterministic decision outcomes under controlled
threshold displacement, not as a causal deployment claim.

## GPT-OSS sensitivity

The GPT-only paired results are reported separately because the observed
metric-error population is strongly concentrated in the model labeled
`gpt` in the frozen Phase 1.5 artifacts.

## Reproducibility

All inputs are already-generated Phase 1.5 CSV files.
No model/API inference was performed.
