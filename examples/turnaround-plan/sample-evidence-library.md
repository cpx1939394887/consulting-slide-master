# Sample Evidence Library

Synthetic data only. This example is not based on any real company.

| data_name | value | period | unit | scope | source | confidence | conflicts | usable_pages |
|---|---:|---|---|---|---|---|---|---|
| Original planned capacity | 4 lines | Plan | lines | board-approved plan | investment memo | high | none | overview, investment review |
| Current built capacity | 2 lines | Current | lines | completed phase one | asset ledger | high | none | overview, asset status |
| Second phase status | not started | Current | status | phase two | asset ledger | high | none | decision page |
| Market selling price | 255 | Current quarter | currency/unit | average realized price | operating data | medium | tax treatment differs by source | market reset, margin bridge |
| Planned selling price | 580 | Original plan | currency/unit | plan assumption | investment memo | high | none | market reset |
| Revenue | 12.8 | Current quarter | million | actual operating revenue | operating data | high | none | financial overview |
| Gross profit | -0.6 | Current quarter | million | actual operating gross profit | operating data | high | none | financial overview, margin page |
| Unit gross margin | -9 | Current quarter | currency/unit | actual unit gross margin | operating data | high | none | margin page |
| Operating cash flow | 3.3 | Current quarter | million | actual operating cash flow | cash report | high | none | financial overview |
| Net profit | -3.2 | Current quarter | million | actual net profit | operating data | high | none | financial overview |
| Finance cost | 2.3 | Current quarter | million | internal loan cost | finance ledger | medium | loan balance requires final finance confirmation | three-hurdle page |
| Utilization rate | 28 | Current quarter | percent | actual output / effective capacity | operating data | medium | capacity definition differs from plan | utilization page |
| Logistics disadvantage | high | Current | qualitative | distance to core market | sales interviews | medium | none | cost structure |
| Customer credit constraint | material | Current | qualitative | cash sales vs market credit terms | sales interviews | medium | none | sales model |

## Source Discipline Notes

- Price values are synthetic and expressed as currency per unit.
- Amounts are synthetic and expressed in millions.
- Any conflicting definition is intentionally marked rather than resolved silently.

