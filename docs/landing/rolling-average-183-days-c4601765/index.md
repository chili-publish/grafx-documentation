---
hide:
  - navigation
  - toc
---

# Your 6-month rolling average

Your subscription measures render usage against your quota using a **6-month rolling average**.

In practice, that average is calculated over a **rolling window of 183 days** — not over six calendar months.

## Why days instead of calendar months

Calendar months are not equal in length. February has 28 days, January has 31. If the calculation used calendar months, your average would move up and down purely because of the calendar, without your production changing at all.

To avoid that, CHILI GraFx uses a fixed window of days.

!!! Formula

    **Window** = the last 183 days, counted back from today

    **Rolling average** = total of past 183 days divided by 6

## What this means for you

- **The window moves every day.** Each day, one day drops off the back and today is added at the front. Your average can change slightly from one day to the next even if you produce nothing.
- **A single busy day stays in the calculation for 183 days.** A large campaign will keep lifting your average for roughly six months, then drop out of the window on its own.
- **Month boundaries don't reset anything.** There is no "start of the month" moment where usage is cleared.
- **Your dashboard shows usage with a delay of ±1 day.** Today's output typically appears tomorrow.

## How this relates to your quota

Render quota are not a hard limit per month. If you generate more output than the render quota, we won't block or watermark the output.

We take your **contractual** rolling average and compare it to your quota:

- If the rolling average remains below the contract, nothing will change.
- When the rolling average exceeds the render quota, you will be invoiced an extra render pack to increase your render quota to at least the average.

This is why seasonal peaks are usually absorbed without any change to your subscription. There is no hard limit, so you can always burst to much higher than your quota — and the spike is divided across the full 183-day window, which flattens its effect on the average considerably.

!!! info "Check your own numbers"

    Your dashboard shows the actual status of renders for the full subscription (all environments). The light blue line on the render graph is the rolling average.

## Checking the period via the API

The Platform API reports both the average and the number of days it was calculated over:

```
GET /api/v1/subscriptions/{subscriptionId}
```

| Property | Meaning |
|---|---|
| `averageRenders` | Your rolling average of renders |
| `averageWatermarkedRenders` | Your rolling average of watermarked renders |
| `averageRendersPeriodDays` | The averaging period in days — `183` for your subscription |

`usedRenders` and `usedWatermarkedRenders` are deprecated in favour of `averageRenders` and `averageWatermarkedRenders`. The `avgPerMonths` query parameter is deprecated as well.

## Related

- [Renders](/CHILI-GraFx/concepts/renders/)
- [Subscriptions](/CHILI-GraFx/concepts/subscriptions/)
