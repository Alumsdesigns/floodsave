# Hypothesis Validation
## What this is
Three hypotheses about Irish flood risk were defined before 
modelling began. Each is tested using a statistical method 
appropriate to the variable types. Results are documented in 
Notebook 05 and displayed on the Hypothesis Validation 
dashboard page.

## Why it matters
- Criteria 1.2 (Merit) requires hypotheses stated in README
- Criteria 2.3 (Merit) requires statistical validation
- Criteria 4.3 (Merit) requires conclusions on dashboard
- Criteria D3 (Distinction) requires 3+ hypotheses validated
- A failed hypothesis is still valid — what matters is the 
  statistical test was run and the result is explained

```mermaid
graph TD
    classDef hyp  fill:#1565C0,color:#fff,stroke:#0D47A1
    classDef test fill:#E65100,color:#fff,stroke:#BF360C
    classDef pass fill:#2E7D32,color:#fff,stroke:#1B5E20
    classDef fail fill:#B71C1C,color:#fff,stroke:#7F0000

    H1["Hypothesis 1
    ─────────────
    Properties below 10m elevation
    have significantly higher flood
    risk than those above 10m"]:::hyp

    H2["Hypothesis 2
    ─────────────
    Distance to nearest river is
    the strongest predictor of
    flood risk classification"]:::hyp

    H3["Hypothesis 3
    ─────────────
    Western counties have higher
    average flood depth than
    Eastern counties"]:::hyp

    T1["Chi-square test
    ─────────────
    elevation_category
    vs flood_risk_class"]:::test

    T2["Feature importance
    + Independent t-test
    ─────────────
    distance_to_river
    within 500m vs beyond"]:::test

    T3["Independent t-test
    ─────────────
    West county region
    vs East county region
    on max_flood_depth"]:::test

    PASS["Validated
    ─────────────
    p less than 0.05
    Documented in README
    and dashboard page"]:::pass

    FAIL["Not Supported
    ─────────────
    p greater than 0.05
    Still valid outcome
    Explained in dashboard"]:::fail

    H1 --> T1
    H2 --> T2
    H3 --> T3
    T1 --> PASS
    T1 --> FAIL
    T2 --> PASS
    T2 --> FAIL
    T3 --> PASS
    T3 --> FAIL
```
