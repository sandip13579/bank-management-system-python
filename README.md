Bank Management System (Python)

 Approach & Design Thinking -:

While building this project, my main focus was not just to implement functionality, but to design the system using proper Object-Oriented Programming principles.

I started by identifying the core entities of the system — **Account** and **Bank** — and clearly defined their responsibilities.
The `Account` class handles all account-related operations such as deposit, withdrawal, balance management, and PIN verification, while the `Bank` class is responsible for managing multiple accounts and handling operations like account creation and search.

One of my key goals was to implement **encapsulation** effectively. Sensitive data such as account balance and PIN were kept private, and all operations were performed through methods like `deposit()`, `withdraw()`, and `check_pin()` instead of direct access.

I also focused on creating a **real-world flow** by introducing a menu-driven interface where users can interact with the system, perform transactions, and securely access their accounts using PIN authentication.

Additionally, I handled edge cases such as:

* Preventing duplicate account creation
* Validating deposit and withdrawal amounts
* Handling incorrect PIN entries
* Managing scenarios where an account does not exist

This project helped me strengthen my understanding of how to design scalable and maintainable systems using Python and OOP concepts, rather than just writing procedural code.

