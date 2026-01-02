# Massive.com API – Benzinga Feeds

**Base URL**: https://api.massive.com  
**Rate Limit**: 5 calls/minute (plan limit)  
**Status**: Endpoints untested

## News & Sentiment
- GET /benzinga/v2/news — News articles
- GET /benzinga/v1/analyst-insights — Analyst insights

## Ratings & Analysis
- GET /benzinga/v1/analysts — Analyst directory
- GET /benzinga/v1/ratings — Analyst ratings
- GET /benzinga/v1/consensus-ratings/{TICKER} — Consensus ratings
- GET /benzinga/v1/firms — Firm details

## Corporate Actions
- GET /benzinga/v1/earnings — Earnings calendar
- GET /benzinga/v1/guidance — Corporate guidance

## Data Notes
- Coverage: Benzinga fundamental and news datasets
- Update frequency: Near real-time

## Testing Status
- Endpoints not yet exercised in this workspace
