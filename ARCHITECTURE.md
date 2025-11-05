# Application Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        DAIGAKU APPLICATION                           │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE LAYER                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐         ┌───────────────────────────────────┐   │
│  │ LoginWindow  │────────>│        MainWindow                  │   │
│  │              │         │  ┌─────────────┬─────────────────┐ │   │
│  │ - Username   │         │  │ Flashcards  │ Immersion Mats  │ │   │
│  │ - Password   │         │  │   Widget    │     Widget      │ │   │
│  │ - DB Config  │         │  └─────────────┴─────────────────┘ │   │
│  └──────────────┘         │                                     │   │
│         │                  │  - Menu Bar                        │   │
│         │                  │  - Status Bar                      │   │
│         │                  │  - User Info                       │   │
│         │                  └───────────────────────────────────┘   │
│         ▼                                  │                        │
│  Authentication                            │                        │
│         │                                  │                        │
└─────────┼──────────────────────────────────┼────────────────────────┘
          │                                  │
          ▼                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        BUSINESS LOGIC LAYER                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────────┐              ┌─────────────────┐              │
│  │ FlashcardWidget │              │ ImmersionWidget │              │
│  ├─────────────────┤              ├─────────────────┤              │
│  │ - Deck Select   │              │ - Material List │              │
│  │ - Card Display  │              │ - Add Material  │              │
│  │ - Show Answer   │              │ - Log History   │              │
│  │ - Rate Quality  │              │ - View Details  │              │
│  │ - Progress Bar  │              │ - Admin Actions │              │
│  └────────┬────────┘              └────────┬────────┘              │
│           │                                │                        │
│           │    ┌───────────────┐          │                        │
│           └───>│ SRSAlgorithm  │<─────────┘                        │
│                ├───────────────┤                                    │
│                │ - Calculate   │                                    │
│                │   Interval    │                                    │
│                │ - Check Due   │                                    │
│                │ - Priority    │                                    │
│                └───────────────┘                                    │
│                        │                                            │
└────────────────────────┼────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        DATA ACCESS LAYER                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                    DatabaseManager                            │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │  User Methods:                                                │  │
│  │  - authenticate_user()      - get_user_info()                │  │
│  │                                                               │  │
│  │  Flashcard Methods:                                           │  │
│  │  - get_all_decks()          - get_flashcards_by_deck()       │  │
│  │  - get_cards_due_for_review() - record_card_review()         │  │
│  │  - get_card_review_history()                                 │  │
│  │                                                               │  │
│  │  Immersion Methods:                                           │  │
│  │  - get_all_immersion_materials()                             │  │
│  │  - get_user_material_history()                               │  │
│  │  - add_material_to_history()                                 │  │
│  │  - add_immersion_material()                                  │  │
│  │  - delete_immersion_material()                               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                              │                                      │
└──────────────────────────────┼──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         DATABASE LAYER                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                      MySQL Database                           │  │
│  │                        (daigaku)                              │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │                                                               │  │
│  │  ┌─────────┐  ┌──────────┐  ┌───────────────────┐           │  │
│  │  │  user   │  │   deck   │  │    flashcard      │           │  │
│  │  └─────────┘  └──────────┘  └───────────────────┘           │  │
│  │                                                               │  │
│  │  ┌──────────────────┐  ┌─────────────────────────┐          │  │
│  │  │ user_card_review │  │ immersion_material      │          │  │
│  │  └──────────────────┘  └─────────────────────────┘          │  │
│  │                                                               │  │
│  │  ┌────────────────────────┐  ┌──────────────┐               │  │
│  │  │ user_material_history  │  │ vocabulary   │               │  │
│  │  └────────────────────────┘  └──────────────┘               │  │
│  │                                                               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘


DATA FLOW DIAGRAMS
==================

1. LOGIN FLOW
   User Input → LoginWindow → DatabaseManager.authenticate_user()
              → MySQL Query → Result → MainWindow (if success)

2. FLASHCARD REVIEW FLOW
   Select Deck → DatabaseManager.get_cards_due_for_review()
              → SRSAlgorithm.get_card_priority()
              → Display Card → User Rates → record_card_review()
              → Update Database → Next Card

3. IMMERSION LOGGING FLOW
   Browse Materials → Select Material → Click Log
                   → DatabaseManager.add_material_to_history()
                   → Insert to user_material_history → Confirmation

4. ADMIN ADD MATERIAL FLOW
   Click Add → AddMaterialDialog → Fill Details → OK
            → DatabaseManager.add_immersion_material()
            → Insert to immersion_material → Refresh Table


KEY INTERACTIONS
================

┌──────────┐                ┌──────────────┐                ┌──────────┐
│   User   │───── uses ────>│ PyQt5 Widget │───── calls ───>│ Database │
└──────────┘                └──────────────┘                └──────────┘
                                   │                              │
                                   │                              │
                                   ▼                              ▼
                            ┌─────────────┐                ┌──────────┐
                            │ SRS Logic   │                │  MySQL   │
                            └─────────────┘                └──────────┘


FILE DEPENDENCIES
=================

main.py
  └── login_window.py
        └── database.py ──────┐
              └── config.py    │
                               │
  └── main_window.py           │
        ├── flashcard_widget.py│
        │     └── srs_algorithm.py
        │     └── database.py ─┤
        │                      │
        └── immersion_widget.py│
              └── database.py ─┴─> MySQL Connector
                                    └── mysql.connector


CONFIGURATION FLOW
==================

config.ini ──> config.py ──> DatabaseManager ──> MySQL Connection
                          └─> LoginWindow (defaults)


THREAD/PROCESS MODEL
====================

Main Thread:
  - PyQt5 Event Loop
  - UI Updates
  - User Interactions

Database Operations:
  - Synchronous queries
  - Connection pooling
  - Transaction management

Background (Future):
  - Could add async for large queries
  - Image/audio loading
  - Cloud sync
```
