# SAT Solving for Students

An educational workshop developed to introduce high-school students to **propositional satisfiability (SAT)** through implementing a simple SAT solver in Python.

Rather than treating SAT solving as a black box, participants gradually build a complete SAT solver from scratch while learning the underlying algorithms and data structures.

## Learning objectives

After completing the workshop, participants will understand

- propositional logic
- conjunctive normal form (CNF)
- the SAT problem
- efficient variable and literal encodings
- recursive backtracking
- watchlists for efficient conflict detection
- how a basic SAT solver works internally

## Workshop contents

The repository contains

- 📄 a complete workshop handout
- 💻 a reference implementation of a SAT solver in Python
- 📝 implementation exercises
- 📂 several example SAT instances
- 🕵️ a logical reasoning example based on witness statements

## SAT Solver

Participants implement a complete SAT solver capable of

- parsing CNF formulas,
- representing variables and literals efficiently,
- solving SAT instances using recursive backtracking,
- using a watchlist-based propagation mechanism to prune the search space,
- enumerating all satisfying assignments.

The resulting solver is intentionally simple and designed for educational purposes rather than maximum performance.

## Background

This workshop is based on the ideas presented in Sahand Saba's article
[*Understanding SAT by Implementing a Simple SAT Solver in Python*](https://sahandsaba.com/understanding-sat-by-implementing-a-simple-sat-solver-in-python.html).

The implementation has been adapted and expanded into a structured educational workshop with original teaching material, implementation exercises and additional example problems.

## Target audience

- High-school students interested in computer science
- Undergraduate students learning SAT solving
- Anyone interested :)

## References

Sahand Saba.
*Understanding SAT by Implementing a Simple SAT Solver in Python.*

https://sahandsaba.com/understanding-sat-by-implementing-a-simple-sat-solver-in-python.html
