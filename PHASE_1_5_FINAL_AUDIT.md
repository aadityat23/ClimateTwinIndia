# ClimateTwin Phase 1.5 — Final Research Audit

## Status

**Phase 1.5 is FROZEN.**

No further experimental changes should be made to the Phase 1.5
scientific artifacts unless a new explicitly numbered phase is opened.

This document records the final state of the Phase 1.5 evidence chain,
the reproducibility boundary, and known interpretation limits.

---

# 1. Scope

Phase 1.5 evaluates the sensitivity of deterministic ClimateTwin
Hypothesis benchmark decisions to controlled displacement of the
decision thresholds used by the canonical ground-truth evaluator.

The analysis is performed offline from already-generated benchmark and
model-evaluation artifacts.

No model/API inference was performed during Phase 1.5D–G.

---

# 2. Frozen evidence chain

Phase 1.5 consists of four analytical stages.

## Phase 1.5D — Decision-margin sensitivity

Primary intervention:

    T'(alpha) = T + alpha * (GT_metric - T)

where:

- T is the canonical threshold,
- GT_metric is the canonical ground-truth metric,
- alpha controls contraction toward the canonical GT metric.

Frozen alpha grid:

    [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]

The canonical decision function is reused rather than reimplemented.

Metric-error observations:

    N = 245

Baseline propagation:

    56.3265%

Toward-GT propagation at alpha=.99:

    68.9796%

Absolute change:

    +12.6531 percentage points

Canonical GT decisions changed through alpha=.99:

    0

---

# 3. Phase 1.5E — Directional control

A matched control displaces thresholds away from the canonical
ground-truth metric by the same alpha schedule.

The control is designed to test whether the observed effect is merely
a generic consequence of perturbing thresholds.

Metric-error observations:

    N = 245

Away-GT propagation at alpha=.99:

    41.2245%

Toward-GT propagation at alpha=.99:

    68.9796%

Toward-minus-away difference:

    +27.7551 percentage points

Canonical GT decisions changed through alpha=.99:

    0

---

# 4. Phase 1.5F — Statistical inference

The original paired endpoint uses exact two-sided McNemar testing.

## Primary comparison

Baseline → Toward-GT alpha=.99

Baseline:

    56.3265%

Toward:

    68.9796%

Paired difference:

    +12.6531 pp

95% bootstrap CI:

    [+4.49, +20.41] pp

Exact two-sided McNemar p:

    0.0026537861

Discordant pairs:

    absorbed → propagated = 66
    propagated → absorbed = 35

## Directional comparison

Away-GT alpha=.99 → Toward-GT alpha=.99

Away:

    41.2245%

Toward:

    68.9796%

Difference:

    +27.7551 pp

95% bootstrap CI:

    [+20.00, +35.51] pp

Exact two-sided McNemar p:

    3.7651773e-11

Discordant pairs:

    away propagated → toward absorbed = 21
    away absorbed → toward propagated = 89

Bootstrap:

    10,000 resamples

Seed:

    20260626

---

# 5. Phase 1.5G — Mixed-effects robustness

Phase 1.5G re-evaluates the frozen endpoints using a binomial
generalized linear mixed model with a question-level random intercept.

The original paired McNemar analyses remain the primary statistical
analysis. The mixed-effects models are robustness analyses and do not
replace the frozen endpoint.

## Baseline → Toward

Pairs:

    245

Mixed-model odds ratio:

    1.838698

95% interval:

    [1.384961, 2.441086]

Posterior probability beta > 0:

    0.999987

Question random-intercept SD:

    0.736829

## Away → Toward

Pairs:

    245

Mixed-model odds ratio:

    3.843138

95% interval:

    [2.877542, 5.132751]

Posterior probability beta > 0:

    1.000000

Question random-intercept SD:

    0.910654

---

# 6. GPT-OSS-120B label clarification

The canonical internal evaluation label:

    gpt

corresponds to:

    GPT-OSS-120B

This mapping is explicitly present in the existing evaluation
infrastructure:

    "GPT-OSS-120B": "gpt"

and the evaluator also contains the model identifier:

    gpt_oss_120b

The historical `gpt` filename and result label therefore MUST NOT be
renamed as part of Phase 1.5.

For interpretation, references to the `gpt` subset in Phase 1.5G should
be read as the canonical GPT-OSS-120B evaluation label.

The error-conditioned population is strongly concentrated in this
model:

    GPT-OSS-120B / gpt = 230 observations
    DeepSeek          = 14 observations
    Claude            = 1 observation

Therefore Phase 1.5 must NOT be described as an equally balanced
five-model robustness experiment.

---

# 7. GPT-OSS-120B sensitivity check

The existing Phase 1.5G sensitivity analysis reports:

Primary GPT-only paired McNemar:

    p = 0.012400603

Directional GPT-only paired McNemar:

    p = 1.015826e-10

These results are reported as a model-concentration sensitivity check,
not as evidence of balanced cross-model replication.

---

# 8. Alpha=1.0 boundary diagnostic

Alpha=1.0 is intentionally excluded from the frozen sensitivity grid.

The frozen grid ends at:

    alpha = 0.99

The canonical GT decision remains unchanged throughout this frozen
range.

The previously circulated value:

    222 / 245

for alpha=1.0 canonical GT decision changes is NOT independently
reproducible from the frozen question-level sensitivity CSV alone.

The frozen CSV does not preserve sufficient underlying
metric/threshold state to independently reconstruct the canonical
oracle at alpha=1.0.

Therefore:

**222/245 MUST NOT be presented as a verified Phase 1.5 result.**

The reproducible statement is:

> Canonical ground-truth decisions remained unchanged throughout the
> tested perturbation range alpha <= 0.99.

Alpha=1.0 is an equality-boundary diagnostic outside the frozen
inferential endpoint.

---

# 9. Interpretation boundary

The evidence supports claims about:

- deterministic decision sensitivity,
- controlled threshold displacement,
- directional contrast between toward-GT and away-GT perturbations,
- paired statistical association between threshold displacement and
  decision outcome,
- robustness to question-level clustering.

The evidence does NOT by itself establish:

- causal deployment effects,
- generalization to arbitrary threshold changes,
- generalization to unseen benchmark protocols,
- balanced robustness across all evaluated models,
- superiority in real-world deployment,
- that the threshold intervention is representative of every possible
  protocol modification.

These distinctions must be preserved in any paper, presentation,
review response, or external communication.

---

# 10. Reproducibility boundary

All Phase 1.5D–G analyses operate on existing artifacts.

Primary inputs include:

    benchmark/ClimateTwinBench_Hypothesis_V2.json

    experiments/experiment_05_derivation/results/*_derivation.csv

    experiments/experiment_05_derivation/results/margin_sensitivity/

    experiments/experiment_05_derivation/results/margin_sensitivity_control/

The statistical analysis consumes already-generated CSV artifacts.

No new model inference is required.

---

# 11. Frozen outputs

## Phase 1.5D

    results/margin_sensitivity/
        question_level_sensitivity.csv
        aggregate_sensitivity_overall.csv
        aggregate_sensitivity_by_model.csv
        aggregate_sensitivity_by_category.csv
        margin_sensitivity_metadata.json

## Phase 1.5E

    results/margin_sensitivity_control/
        question_level_control.csv
        aggregate_control_overall.csv
        aggregate_control_by_model.csv
        aggregate_control_by_category.csv
        margin_sensitivity_control_metadata.json

## Phase 1.5F

    results/phase_1_5f_statistics/
        phase_1_5f_alpha_curve.csv
        phase_1_5f_category_effects.csv
        phase_1_5f_directional_effect.csv
        phase_1_5f_model_effects.csv
        phase_1_5f_primary_effect.csv
        phase_1_5f_report.md
        phase_1_5f_statistics.json

## Phase 1.5G

    results/phase_1_5g_mixed_effects/
        phase_1_5g_mixed_effects_summary.csv
        phase_1_5g_gpt_sensitivity.csv
        phase_1_5g_report.md
        phase_1_5g_metadata.json

## Alpha=1 diagnostic

    results/phase_1_5_alpha1_diagnostic/
        phase_1_5_alpha1_diagnostic.csv
        phase_1_5_alpha1_diagnostic.json
        phase_1_5_alpha1_diagnostic.md

---

# 12. Final conclusion

The frozen Phase 1.5 evidence chain shows that, among the 245
model/question observations with an observed metric error, controlled
threshold contraction toward the canonical ground-truth metric is
associated with a higher deterministic propagation rate than baseline,
while the matched away-from-GT control moves in the opposite direction.

The primary endpoint is:

    56.33% → 68.98%
    +12.65 pp
    McNemar p = 0.00265
    mixed-model OR = 1.84
    95% interval = [1.38, 2.44]

The directional control is:

    41.22% away → 68.98% toward
    +27.76 pp
    McNemar p = 3.77e-11
    mixed-model OR = 3.84
    95% interval = [2.88, 5.13]

These findings are interpreted strictly as evidence of deterministic
directional sensitivity under the specified controlled intervention.

Phase 1.5 is therefore considered **FROZEN**.

Further scientific investigation must be opened as a new numbered phase
rather than modifying these artifacts in place.

