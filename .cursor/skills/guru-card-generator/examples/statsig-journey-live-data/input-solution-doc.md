# Real-time Experiment Assignment
## Iterable Journey Live Data & Statsig

> Source: customer solutions doc (PDF). This is the **before** — customer-specific framing and implementation detail as written for a deal.

---

## Purpose

To assign and retrieve real-time experiment assignments from Statsig for downstream routing and personalization within Iterable journeys.

## Context

Currently, customers pre-assign users in experiments with Statsig and then pass those as fields to their data warehouse or system to sync to Iterable as user fields. From there, customers send a campaign to the control group and a different variant to the test group (or not send one). This is to measure whether sending campaigns or a different variant will show lift in conversions or purchases.

Based on the user's activity and behavior, their experiment assignment may change while they're in a journey or after the data sync. A user who was previously in the control group may now be in the test group. However, in this case, this user would receive the control variant when they should've received the test variant.

## Solution

Implement Journey Live Data tile to retrieve real-time experiment assignments from Statsig to filter users in the control and test group. With this solution:

- No need to pre-assign users to experiments
- No middleware setup
- Does not bloat or add to data schema

## Setup

### Create Iterable Journey Webhook

1. In Statsig, Settings > Keys & Environment, create a new or copy the Server Secret Key (`secret-...`). This will need to be used in the below steps.
2. In Iterable, create a journey webhook (Integrations > Journey Webhooks).
   a. Name the webhook (internal)
   b. **Request section**
      - Destination: Custom
      - Method: POST
      - Endpoint: `https://api.statsig.com/v1/get_config`
      - Authentication: None
      - Rate limit: 250 calls per second (recommended)
      - Custom headers (2):
        1. Name: `statsig-api-key`, Value: `YOUR-SECRET-KEY` (from step 1)
        2. Name: `Content`, Value: `application/json`
      - Body:
        - In drop-down, select JSON
        - Payload:
          ```json
          {
            "configName": "abandon_cart",
            "user": {
              "userId": "{{userId}}"
            }
          }
          ```
        - `configName` is the Statsig Experiment ID.
      - Be sure that "Include all triggering event fields and workflowId" is **unchecked**
   c. **Data Retrieval**
      - Check the box for "Fetch external data to use journeys"
      - To run a test, change the `userId` to an actual userId (Payload above).
      - Click on "Run Test"
      - This should show "Webhook test successful" with the Response payload:
        ```json
        {
          "name": "abandon_cart",
          "value": { "active": false },
          "group": "413e6jHXeUcxIHLr5w3JzS",
          "rule_id": "413e6jHXeUcxIHLr5w3JzS",
          "group_name": "Test"
        }
        ```
      - If experiencing errors, check the `configName` to ensure that the value matches the Experiment ID in Statsig.
      - Select the "Live Data" fields you'd like to use for filtering and personalization (i.e. `name`, `groupName`).
      - Change the value for `userId` back to `{{userId}}` in the payload.

### Add Live Data Tile to Journey

1. Create a journey and add a Live Data tile.
2. Select the webhook you've created from the above steps.
3. Add any filter tiles to reference these Live Data fields for downstream routing and message tiles in handlebar logic for dynamic personalization.

## Test

1. Click on Test Journey.
2. Select `userId` and enter a sample userId.

## Example Journey

(Screenshots of journey canvas with Live Data tile, filter branches for Control vs. Test, and message tiles.)
