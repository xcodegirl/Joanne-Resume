# T0510 — ASP.NET Core
**Program:** Full Stack Development (FSD)  
**Hours:** 60 hrs (3 weeks)  
**Delivery:** Online Instructor-Guided

---

## Description

Students develop full-stack web applications using ASP.NET Core. Building on earlier .NET and C# coursework, students integrate front-end interfaces with back-end business logic and database persistence. Topics include Razor Pages, middleware, authentication and authorisation, and deployment to a web host.

---

## Learning Outcomes

**Outcome 1: Build web applications using ASP.NET Core Razor Pages**
- Describe the Razor Pages request lifecycle
- Create page models with GET and POST handlers
- Use tag helpers to generate forms and links
- Bind form data to page model properties
- Implement server-side and client-side validation
- Apply layout pages and partial views for consistent structure

**Outcome 2: Implement middleware, authentication, and authorisation**
- Describe the ASP.NET Core middleware pipeline
- Register and configure middleware components
- Implement cookie-based authentication using ASP.NET Core Identity
- Protect pages and routes using authorisation attributes
- Manage user roles and claims
- Apply security best practices: CSRF protection, HTTPS enforcement

**Outcome 3: Integrate a database and deploy a complete web application**
- Review Entity Framework Core within an ASP.NET Core context
- Scaffold CRUD pages from an EF Core model
- Implement a repository or service layer to separate concerns
- Configure connection strings for development and production
- Publish an ASP.NET Core application to a web host (Azure App Service or equivalent)
- Perform post-deployment smoke testing

---

## Assessment

| Assessment | Description | Weight |
|---|---|---|
| Assignment 1: Razor Pages Application | Multi-page application with forms, validation, and layout | 33% |
| Assignment 2: Authentication & Authorisation | Add identity, login/logout, and role-based page protection | 33% |
| Assignment 3: Full-Stack App + Deployment | Integrate database, complete CRUD, and deploy to cloud | 34% |

**Minimum passing grade:** 70%

### Assessment → Outcome Mapping

| Assessment | LO1 Razor Pages | LO2 Auth | LO3 DB + Deploy |
|---|:---:|:---:|:---:|
| Assignment 1 | ✓ | | |
| Assignment 2 | | ✓ | |
| Assignment 3 | | | ✓ |

---

## Course Schedule

### Module 1 — Razor Pages (Week 1, 20 hrs)

**Topics:**
- ASP.NET Core project structure and startup pipeline
- Razor Pages vs MVC: choosing a model
- Page models: `OnGet`, `OnPost`, `BindProperty`
- Tag helpers: `asp-for`, `asp-action`, `asp-controller`
- Data annotations and model validation
- Layout pages, sections, and partial views
- Dependency injection fundamentals

**Activities:**
- Scaffold a Razor Pages project; explore file layout
- Build a multi-page site with shared layout
- Create a form with server-side validation and error display
- Inject a simple service into a page model

---

### Module 2 — Middleware, Authentication, and Authorisation (Week 2, 20 hrs)

**Topics:**
- Middleware pipeline: `Use`, `Run`, `Map`
- Custom middleware: logging, error handling
- ASP.NET Core Identity: setup and scaffolding
- Registration, login, logout, and password hashing
- `[Authorize]` and `[AllowAnonymous]` attributes
- Roles: assigning and checking role membership
- CSRF tokens and anti-forgery with Razor Pages
- HTTPS redirection and HSTS

**Activities:**
- Add custom request logging middleware
- Scaffold Identity into an existing project
- Protect a page behind `[Authorize]`
- Create an admin role and restrict a management page

---

### Module 3 — Database Integration and Deployment (Week 3, 20 hrs)

**Topics:**
- EF Core in ASP.NET Core: `AddDbContext`, connection strings
- Scaffolding CRUD Razor Pages from a model
- Service/repository layer: separating data access from page models
- Migrations in a team/CI context
- Azure App Service: creating a resource, configuring connection string, publishing
- Environment-specific configuration (`appsettings.Production.json`)
- Smoke testing a deployed application

**Activities:**
- Add EF Core and scaffold CRUD pages
- Refactor scaffolded code into a service class
- Configure an Azure App Service and SQL database
- Publish via VS or GitHub Actions pipeline
- Verify deployed app with end-to-end walkthrough

---

## Required Materials

- **Textbook:** Drescher, T., Zuker, A., & Friedman, S. (2018). *Hands-On Full Stack Web Development with ASP.NET Core.* Packt.
- **Software:** Visual Studio 2022 or VS Code; .NET SDK (latest LTS); Azure subscription (free tier)
- **Equipment:** Laptop/Computer

---

## Academic Policies

- **Grading:** Minimum 70% to pass
- **Attendance:** Active participation is tracked
- **Copyright:** Unauthorized copies of course materials are a violation of the Copyright Act and may constitute academic misconduct
- See the [Robertson College Student Guide](https://www.robertsoncollege.com/help/student-resources/student-guide/) for full policies
