# Tactical Playbook: Doing Things That Don't Scale

"Do things that don't scale" is the golden rule of early-stage startups. This document provides a library of manual tactics based on historical unicorn success stories.

## Core Philosophy

### Why "Do Things That Don't Scale"?

**The Anti-Automation Logic of the Early Stage**:
- ❌ **Premature optimization is the root of all evil**.
- ❌ Writing a scheduling algorithm before you have users is a waste.
- ❌ Implementing automation before establishing trust leads to failure.
- ✅ Manual operations allow for rapid hypothesis validation.
- ✅ Hands-on work builds deep user understanding.
- ✅ Human service establishes early trust and word-of-mouth.

### When to Stop Manual Tactics?

**Tipping Point Signals**:
1. Manual operations become the primary bottleneck to growth.
2. You have reached a stable 5-7% weekly growth rate.
3. Unit economics (LTV/CAC) are validated.
4. The team physically cannot handle the user volume.

**Progressive Automation**:
- It's not a sudden jump from 100% manual to 100% automated.
- Gradually identify the most time-consuming yet low-value links.
- Prioritize automating highly repetitive tasks.

## Classic Tactical Case Library

### 1. Stripe: The Collison Installation

**The Tactic**:
- Founders Patrick and John Collison would literally take over a user's laptop on the spot.
- They wrote the code to integrate the API themselves.
- Users went from "interested" to "live and running" in 10 minutes.

**Core Value**:
- Eliminated all friction.
- Received immediate product feedback.
- Built deep early customer trust.

**Agent Recommendation Template**:
> **Scenario**: User says, "I sent out invite codes but nobody is registering."
> 
> **Response**: "Stop mass mailing. Adopt the **Collison Installation**:
> 1. Filter the top 5 most promising target customers.
> 2. Schedule a video call or an in-person visit.
> 3. Take over their keyboard and complete registration/setup for them.
> 4. Ensure they complete their first 'success moment' during the call.
> **Goal**: Not 100 lukewarm signups, but 5 fanatical users."

### 2. Airbnb: Manual Photography Service

**The Tactic**:
- In 2009, Airbnb growth stalled.
- The founders realized low-quality listing photos were killing conversion.
- Brian Chesky and Joe Gebbia flew to NYC.
- They went door-to-door to hosts' homes with a rented professional camera and took high-res photos themselves.

**Result**:
- NYC bookings immediately doubled.
- They discovered the product's core pillars: trust and visual presentation.

**Agent Recommendation Template**:
> **Scenario**: User complains, "Content quality on the platform is low, lead conversion is poor."
> 
> **Response**: "Don't wait for users to improve. Adopt the **Airbnb Photography Method**:
> 1. Identify the top 20 high-potential users/merchants.
> 2. Go and produce perfect content for them personally (Photos, copy, optimization).
> 3. Set a 'Trust Standard' based on these manual cases.
> 4. Use these 20 perfect cases to attract and benchmark new users.
> **Goal**: Set the bar yourself rather than waiting for users to spontaneously improve."

### 3. DoorDash: Founder Delivery

**The Tactic**:
- Initially, there were no drivers or dispatch systems.
- They built a static landing page with just a few PDF menus and a founder's personal cell number.
- Founder Stanley Tang personally drove to restaurants and delivered food for months.

**Core Value**:
- Validated real demand for food delivery.
- Understood every friction point in the delivery experience.
- Accumulated the practical experience needed to design the eventual algorithm.

**Agent Recommendation Template**:
> **Scenario**: User says, "I need 3 months to develop a dispatch algorithm/matching system."
> 
> **Response**: "You don't have a single order; you don't need an algorithm. Adopt the **Wizard of Oz MVP**:
> 1. Create the simplest front-end (even a Google Form).
> 2. Leave your personal phone number.
> 3. Act as the algorithm yourself: Manually take orders, manually match, and personally provide the service.
> 4. Serve the first 10 orders and document every pain point.
> **Goal**: Use yourself as a human dispatch system to validate hypotheses."

### 4. Reddit: Founder Socks (Fake It 'Til You Make It)

**The Tactic**:
- Early Reddit had no users.
- The founders created numerous "sock-puppet" accounts.
- They posted, commented, and upvoted their own content to create the illusion of a vibrant community.

**Core Value**:
- Solved the "Cold Start" problem.
- Established the quality benchmark for content.
- Defined the community culture from Day 1.

**Agent Recommendation Template**:
> **Scenario**: Cold-starting a community or platform.
> 
> **Response**: "Adopt the **Reddit Sock-Puppet Tactic**:
> 1. Create 5-10 accounts within the founding team.
> 2. Post high-quality content daily.
> 3. Manufacture interaction: Comments, upvotes, discussions.
> 4. Set the tone and cultural norms.
> 5. Gradually withdraw as real users take over.
> **Warning**: This is 'benevolent deception'—only for the cold start phase.
> **Goal**: Cross the 'Empty Room Dilemma' (nobody wants to be the first person in an empty bar)."

## Tactical Matrix by Business Model

| Model | Automation Fantasy | Recommended Manual Tactic | Reference |
| :--- | :--- | :--- | :--- |
| **B2B SaaS** | Self-serve onboarding | **Collison Installation**: In-person setup | Stripe |
| **Marketplaces** | Algorithmic matching | **Manual Market-making**: Founders act as supply/demand | Airbnb, Etsy |
| **O2O Services** | Intelligent dispatch | **Wizard of Oz MVP**: Founder as backend | DoorDash, Instacart |
| **Communities** | Recommendation Algos | **Manual Curation**: Founders manually handpick content | Pinterest, Reddit |
| **Social Apps** | Viral loops | **Geographic Seeding**: Conquer one campus/office at a time | Tinder, Facebook |
| **Pro Tools** | In-app walkthroughs | **White-Glove Onboarding**: 1-on-1 training | Superhuman |

## Against "Pseudo-Manual" Tactics

### What is Pseudo-Manual?

❌ **Wrong Practices**:
- Mass "personalized" emails (looks manual, is automated).
- Using chatbots to pretend to be human support.
- Templated "personalized" services.

✅ **Truly Manual**:
- Founders are personally involved.
- Every interaction is unique to the user.
- Real relationships are built.

## When to Use Manual Tactics?

### Decision Tree

```
Should we operate manually?

├─ Users < 100?
│  └─ ✅ MANDATORY Manual
│
├─ Users 100 - 1,000?
│  ├─ Do we understand user pain points?
│  │  ├─ No → ✅ Continue Manual
│  │  └─ Yes → Begin Progressive Automation
│  │
│  └─ Retention < 40%?
│     └─ ✅ Back to Manual (Deep Interviews)
│
└─ Users > 1,000?
   ├─ Growth < 5%?
   │  └─ ✅ Pause Scaling, return to Manual Diagnosis
   │
   └─ Growth > 5%?
      └─ ⚠️ Start automating the bottleneck
```

## Common Objections & Counters

### "This doesn't scale."
**Navigator**: "That's exactly the point! In the early stage, scalability is your enemy. You don't need 1,000 lukewarm users; you need 10 users who absolutely love you. Scale is a tomorrow problem. The today problem is: Does anyone actually want this?"

### "I'm a technical founder, not a salesperson."
**Navigator**: "Actually, because you're the founder, you MUST do the selling. A salesperson can tell you 'they didn't buy.' Only you can understand 'why they didn't buy.' Product-Market Fit isn't found in an office; it's found in 100 conversations with customers."

## Key Principles Summary

1. **Scalability is the Enemy (Early On)**: Focus on depth, not breadth.
2. **Founder Must Be in the Trenches**: Cannot delegate early validation.
3. **Manual Insight Accumulation**: Experience defines future automation.
4. **Build Trust, then Standards**: Perfect early cases attract the next 1,000.
5. **Progressive Automation**: Only automate when manual work becomes a growth blocker.
