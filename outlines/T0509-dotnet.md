# T0509 — .NET Programming
**Program:** Full Stack Development (FSD)  
**Hours:** 60 hrs (3 weeks)  
**Delivery:** Online Instructor-Guided

---

## Description

Students gain a comprehensive introduction to .NET programming with C#. The course covers RESTful API development and database integration using Entity Framework Core, culminating in the construction of a complete backend to serve as the business logic layer of a full-stack web application.

---

## Learning Outcomes

**Outcome 1: Create a .NET application using the MVC design pattern**
- Describe the Model-View-Controller (MVC) design pattern
- Configure application settings, appsettings.json, and environment variables
- Create controllers to handle routing and HTTP request processing
- Create models to represent data and business logic
- Create views using Razor templates
- Implement error handling and validation in an MVC application

**Outcome 2: Develop RESTful APIs with ASP.NET Core Web API**
- Describe RESTful API design principles and HTTP verbs (GET, POST, PUT, DELETE)
- Build Web API controllers using `[ApiController]` and routing attributes
- Return appropriate HTTP status codes and response types
- Serialize and deserialize JSON request and response bodies
- Document API endpoints using Swagger/OpenAPI
- Implement input validation and error handling in API responses

**Outcome 3: Integrate databases using Entity Framework Core**
- Describe Object-Relational Mapping (ORM) concepts
- Install and configure Entity Framework Core in a .NET project
- Define `DbContext` and entity classes to represent database tables
- Write LINQ queries to retrieve, filter, and sort data
- Create, apply, and manage database migrations
- Implement full CRUD operations using EF Core

---

## Assessment

| Assessment | Description | Weight |
|---|---|---|
| Assignment 1: MVC Application | Build a working MVC application | 33% |
| Assignment 2: RESTful API | Design and implement a RESTful API with Swagger documentation | 33% |
| Assignment 3: Database Integration | Connect application to a database using Entity Framework Core; implement full CRUD | 34% |

**Minimum passing grade:** 70%

### Assessment → Outcome Mapping

| Assessment | LO1 MVC | LO2 REST API | LO3 EF Core |
|---|:---:|:---:|:---:|
| Assignment 1 | ✓ | | |
| Assignment 2 | | ✓ | |
| Assignment 3 | | | ✓ |

---

## Course Schedule

### Module 1 — .NET MVC Application (Week 1, 20 hrs)

**Topics:**
- Introduction to .NET and the C# ecosystem
- MVC architecture: separating concerns
- Controllers, actions, and routing
- Razor views and layout pages
- Models and data binding
- Form processing and validation
- Error handling

**Activities:**
- Set up a .NET project from template; explore folder structure
- Build a controller with multiple action methods
- Create Razor views with dynamic data binding
- Implement a model with data annotations for validation
- Build a simple multi-page MVC site

**Assignment 1 due:** End of Week 1

---

### Module 2 — RESTful APIs with ASP.NET Core Web API (Week 2, 20 hrs)

**Topics:**
- REST principles and HTTP verbs
- Web API controllers and attribute routing
- JSON serialization with `System.Text.Json`
- HTTP status codes and response objects
- Swagger/OpenAPI documentation
- Input validation and error responses

**Activities:**
- Build a Web API controller returning JSON responses
- Test endpoints using Postman or Swagger UI
- Implement all four HTTP verbs
- Add Swagger documentation with response type annotations
- Handle and return meaningful validation errors

**Assignment 2 due:** End of Week 2

---

### Module 3 — Database Integration with Entity Framework Core (Week 3, 20 hrs)

**Topics:**
- ORM concepts and the EF Core workflow
- `DbContext`, entity classes, and navigation properties
- Code-first migrations
- LINQ queries: filtering, sorting, aggregation
- Full CRUD with EF Core
- Connecting EF Core to a Web API

**Activities:**
- Install EF Core, configure `DbContext` and connection string
- Define entity models and create the first migration
- Write LINQ queries for data retrieval
- Implement repository pattern or direct DbContext CRUD
- Integrate database layer into Assignment 2's API

**Assignment 3 due:** End of Week 3

---

## Required Materials

- **Textbook:** Drescher, T., Zuker, A., & Friedman, S. (2018). *Hands-On Full Stack Web Development with ASP.NET Core.* Packt.
- **Software:** Visual Studio 2022 or VS Code with C# extension; .NET SDK (latest LTS); SQL Server Express or SQLite
- **Equipment:** Laptop/Computer

---

## Academic Policies

- **Grading:** Minimum 70% to pass
- **Attendance:** Active participation is tracked
- **Copyright:** Unauthorized copies of course materials are a violation of the Copyright Act and may constitute academic misconduct
- See the [Robertson College Student Guide](https://www.robertsoncollege.com/help/student-resources/student-guide/) for full policies
