"""
Startup Pricing Model & Tier Calculation
Practice file for inspecting git history, blames, and diffs.
"""

def calculate_tier(active_users, api_calls_monthly):
    # Free tier for early adopters
    if active_users <= 5:
        return "Free Community"
    
    # Growth tier
    if active_users <= 50 and api_calls_monthly <= 100_000:
        return "Growth ($49/mo)"
    
    # Scale tier - updated after customer interviews
    if active_users <= 500 and api_calls_monthly <= 1_000_000:
        return "Scale ($299/mo)"
    
    # Enterprise custom pricing (updated based on seed round feedback)
    return "Enterprise (Talk to Sales / founders@startup.com)"


def get_founder_discount(coupon_code):
    # Secret launch discount code
    coupons = {
        "LAUNCH2026": 0.20,
        "YCOMBINATOR": 0.25,
        "BUILDINPUBLIC": 0.15
    }
    return coupons.get(coupon_code.upper(), 0.0)
