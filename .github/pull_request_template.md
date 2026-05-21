## Copilot Security Review

Before merging this PR, use Copilot to review it for AI Agent / Skill security risks, then perform a human review.

Suggested Copilot prompt:

Review this pull request for AI Agent and Skill security risks.

Focus on:
1. prompt injection or instruction hijacking
2. instructions that override system, developer, or user intent
3. hidden side effects or forced tool chaining
4. context, memory, repository, or secret exfiltration behavior
5. dangerous shell/script execution patterns
6. unsafe MCP or tool configurations with overly broad permissions
7. remote loading, unpinned external content, or TOCTOU risks

Please summarize the risks, explain why they matter, and point to the exact lines or snippets that need human review.

Reviewer checklist:
- [ ] I used Copilot to review this PR
- [ ] I checked for prompt injection / instruction hijacking
- [ ] I checked for hidden side effects / tool chaining
- [ ] I checked for context or secret exfiltration risks
- [ ] I checked for dangerous execution or overly broad tool permissions
- [ ] I completed a human review before merge