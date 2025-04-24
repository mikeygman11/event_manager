# Event Manager API – Onboarding Assignment

This repository contains the completed onboarding assignment for the Event Manager Company. The goal of this assignment was to identify, fix, and document five specific API issues related to user management along with the professor's issue mentioned in the lecture. Each fix includes updated application code, improved validation, and corresponding test coverage to ensure sufficient, elegant code.

## Closed Issues

This project addresses the following closed GitHub issues:

- [Issue #1: Fix login error due to unverified email](https://github.com/mikeygman11/event_manager/issues/1)
- [Issue #2: Add robust username validation](https://github.com/mikeygman11/event_manager/issues/2)
- [Issue #3: Enforce password complexity and hashing standards](https://github.com/mikeygman11/event_manager/issues/3)
- [Issue #7: Profile update - handle edge cases for bio and profile_picture_url](https://github.com/mikeygman11/event_manager/issues/7)
- [Issue #8: Improve partial profile updates and field validation](https://github.com/mikeygman11/event_manager/issues/8)
- [Issue #10: Resolve issue shown in instructor video](https://github.com/mikeygman11/event_manager/issues/10)
- [Issue #15: Add comprehensive test coverage (90%+)](https://github.com/mikeygman11/event_manager/issues/15)

Each issue contains a detailed description, steps taken to fix the problem, and the final outcome, including GitHub pull request links and test results.

---

##  Specific Issues Addressed

### Username Validation
I identified and resolved issues related to improper username validation. The validation logic now enforces:
- Length between 3–30 characters
- Only alphanumeric characters and underscores
- Case-insensitive uniqueness

These improvements help prevent malformed usernames and maintain data consistency.

### Password Validation
Passwords are now required to:
- Be at least 8 characters
- Contain uppercase, lowercase, numbers, and special characters
- Be hashed securely using industry standards

This ensures strong authentication security for all user accounts.

### Profile Field Edge Cases
I tested and fixed edge cases for updating the `bio` and `profile_picture_url` fields. The system now supports:
- One-off profile updates
- Website error handling


### Instructor Demonstration Fix
I implemented a fix shown in the instructor video, which dealt with seamlessly API-testing in Swagger

---

##  Deployment

The project can be built and deployed via Docker. A production-ready Docker image is available on DockerHub:

**[View on DockerHub](https://hub.docker.com/repository/docker/mikeygman11/event_manager)**

---

##  Reflection

This assignment was a valuable experience in debugging and strengthening a production-level FastAPI application. I felt like this project really prepared me for the real-world, since you will rarely be told exactly the problems on hand. Rather, I had to test the API using the Swagger web interface and check that the user creation, deleted, and admin endpoints all worked. When they didn't work, I had to fix them. I felt like this was a great experience and was crucial to preparing me for software engineering. Additionally, I got hands-on practice resolving real-world issues related to input validation, authentication, and edge-case handling. Also, writing tests that simulate realistic user behavior taught me the importance of test design in preventing future issues with code.

Working with GitHub’s pull request workflow helped me understand how to properly branch and document work for the professor to review. I found it immensely helpful to be able to track issues in Github and then resolve them while coding. Closing issues with pull requests is how programming occurs in the real-world, so this felt very important and meaningful. It also underscored the importance of maintaining clean, well-tested code when working as part of a larger team. This process has not only improved my technical skills but also made me a more effective contributor in development environments.

