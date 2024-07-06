# Feedback App

A FastAPI application for managing feedback entries, using SQLAlchemy for database operations and pytest for testing.

## Overview

This project implements a simple API for managing feedback entries. It allows users to create feedback entries with scores and comments, and retrieve them from the database.

## Features

- Create new feedback entries with scores and comments.
- Retrieve all feedback entries.
- Retrieve a specific feedback entry by ID.
- Handle validation and error cases for feedback creation.

## Technologies Used

- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
- SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- pytest: A testing framework for Python that makes it easy to write simple tests.
- Vue2: A progressive JavaScript framework for building user interfaces. It is used here for the frontend.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/erpan011J/simple-feedback-app.git
   cd simple-feedback-app
   ```

2. **Build and run the Docker containers:**

   ```bash
   docker-compose up --build -d
   ```

3. **Access the application:**

   - The feedback form can be accessed at http://localhost:8080/.


## Testing
    
    
    ```bash
    cd simple-feedback-app
    docker exec feedback_app_backend pytest
    ```
    
## API Documentation

    Once the application is running, you can access the API documentation (Swagger UI) at:
    - http://localhost:8000/docs
        
```
feedback-app
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ config
│  ├─ description
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  ├─ sendemail-validate.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ main
│  │     └─ remotes
│  │        └─ origin
│  │           ├─ HEAD
│  │           └─ main
│  ├─ objects
│  │  ├─ 00
│  │  │  └─ 0d96901270e2fd2bd2dba4fe354075d3db3b64
│  │  ├─ 01
│  │  │  └─ d234aab25449ec2f75ed9af741b85cb84feb05
│  │  ├─ 02
│  │  │  └─ fe74800a889f4af5ee46a4af61810577940396
│  │  ├─ 05
│  │  │  └─ 245e9ceb0be47081f45fd699d1008e020392b9
│  │  ├─ 19
│  │  │  └─ 396d4a9a98ed1a1b30049fc8ede044131697f1
│  │  ├─ 2b
│  │  │  └─ 9ddf5f8acaa8d82a9f497f29021f1c297aa39d
│  │  ├─ 40
│  │  │  └─ 0179c261d7819e7dc77d6f4982a20009089552
│  │  ├─ 44
│  │  │  └─ 43b95d0b3ae518bd8aabc3cf0a4200e724a3d0
│  │  ├─ 4d
│  │  │  └─ f067e2ac338c5bdcb499558af906ff9fad82ce
│  │  ├─ 4f
│  │  │  └─ 9fae6ff3274a1f7fa5a14946cae6e951f08b6f
│  │  ├─ 50
│  │  │  └─ c53bcc2e2117770773ea96247654f1b14b7c35
│  │  ├─ 57
│  │  │  └─ 320465aff0bbbcca1ecbcd120a69b17680b847
│  │  ├─ 5d
│  │  │  └─ 4f1a6293572054895e83786a0ed05b34298300
│  │  ├─ 73
│  │  │  └─ 7acd694765231dbd2f4307ad71d93c4630fff5
│  │  ├─ 83
│  │  │  └─ b8601237da780409bc43d6b5048302db23865d
│  │  ├─ 86
│  │  │  └─ baa6c8bea4a2477fe4cf38fe60016819c0925a
│  │  ├─ 89
│  │  │  └─ ea0cf20b787dae65c591dbc0acca8ea559c881
│  │  ├─ 8b
│  │  │  └─ 25b6186e77c81143a233cf1ff14404b021d55f
│  │  ├─ 90
│  │  │  └─ 4a10d0eb2448f0cbe04fb2081bed0d31ca53e9
│  │  ├─ 98
│  │  │  └─ e4f9c44effe479ed38c66ba922e7bcc672916f
│  │  ├─ a9
│  │  │  └─ 299fa3d78b26b4ff202f1769e5eaa7152b87a4
│  │  ├─ ad
│  │  │  └─ f46621963a732a999ac50c175d37008661e15e
│  │  ├─ b1
│  │  │  └─ de380961ab510de3c8e0c0d743ef9c83bcd71b
│  │  ├─ bb
│  │  │  └─ c65c0bd7488965c0f46f1f62540ee1000dd268
│  │  ├─ bd
│  │  │  └─ 0646a139892af687599c6be83dde953ca63cfd
│  │  ├─ c4
│  │  │  └─ b83817ff945d0748aa857e63cd8d6f9e471e62
│  │  ├─ d2
│  │  │  ├─ 80de047e8de3d0a3fa85d81e8e6c7c3ca8a70c
│  │  │  └─ 83db5d99c63db8fee76e27983c05b8c4b89fb8
│  │  ├─ e1
│  │  │  └─ 4003060558a0133d2c1dcb1f325cc897819e8e
│  │  ├─ e6
│  │  │  └─ 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│  │  ├─ e7
│  │  │  └─ d6bafa48f50a9354f17cd474cb429561149687
│  │  ├─ ee
│  │  │  └─ 6d2a88079413f85319b84162713d011f67712c
│  │  ├─ f1
│  │  │  └─ 013c1096f23967f235f0c57f89ee4b4da883cf
│  │  ├─ f6
│  │  │  ├─ 1e2acdb4664e5cb7d1d961ddc4690c5246f262
│  │  │  └─ f44ce58096f1991137d8c78b1eb40eeb6318fa
│  │  ├─ fb
│  │  │  └─ c4b07dcef98b20c6f96b642097f35e8433258e
│  │  ├─ fd
│  │  │  └─ 87543a90570e7f589e06e86dfc1b7e20566e73
│  │  ├─ info
│  │  └─ pack
│  └─ refs
│     ├─ heads
│     │  └─ main
│     ├─ remotes
│     │  └─ origin
│     │     ├─ HEAD
│     │     └─ main
│     └─ tags
├─ .gitignore
├─ backend
│  ├─ .pytest_cache
│  │  ├─ .gitignore
│  │  ├─ CACHEDIR.TAG
│  │  ├─ README.md
│  │  └─ v
│  │     └─ cache
│  │        ├─ lastfailed
│  │        ├─ nodeids
│  │        └─ stepwise
│  ├─ alembic
│  │  ├─ env.py
│  │  ├─ README
│  │  ├─ script.py.mako
│  │  └─ versions
│  │     ├─ 2f0dba82890f_add_comment_field_to_feedback.py
│  │     └─ b9acff6151e3_create_table_feedback.py
│  ├─ alembic.ini
│  ├─ app
│  │  ├─ .pytest_cache
│  │  │  ├─ .gitignore
│  │  │  ├─ CACHEDIR.TAG
│  │  │  ├─ README.md
│  │  │  └─ v
│  │  │     └─ cache
│  │  │        ├─ lastfailed
│  │  │        ├─ nodeids
│  │  │        └─ stepwise
│  │  ├─ api
│  │  │  ├─ feedback.py
│  │  │  └─ __init__.py
│  │  ├─ app_config.py
│  │  ├─ crud
│  │  │  ├─ crud.py
│  │  │  └─ __init__.py
│  │  ├─ database
│  │  │  ├─ database.py
│  │  │  └─ __init__.py
│  │  ├─ main.py
│  │  ├─ models
│  │  │  ├─ models.py
│  │  │  ├─ schemas.py
│  │  │  └─ __init__.py
│  │  ├─ test
│  │  │  ├─ conftest.py
│  │  │  ├─ test_feedback.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ dockerfile
│  ├─ pytest.ini
│  ├─ requirements.txt
│  └─ wait-for-db.sh
├─ docker-compose.yml
├─ frontend
│  ├─ .browserslistrc
│  ├─ .eslintrc.js
│  ├─ .git
│  │  ├─ COMMIT_EDITMSG
│  │  ├─ config
│  │  ├─ description
│  │  ├─ HEAD
│  │  ├─ hooks
│  │  │  ├─ applypatch-msg
│  │  │  ├─ applypatch-msg.sample
│  │  │  ├─ commit-msg
│  │  │  ├─ commit-msg.sample
│  │  │  ├─ fsmonitor-watchman.sample
│  │  │  ├─ post-applypatch
│  │  │  ├─ post-checkout
│  │  │  ├─ post-commit
│  │  │  ├─ post-merge
│  │  │  ├─ post-receive
│  │  │  ├─ post-rewrite
│  │  │  ├─ post-update
│  │  │  ├─ post-update.sample
│  │  │  ├─ pre-applypatch
│  │  │  ├─ pre-applypatch.sample
│  │  │  ├─ pre-auto-gc
│  │  │  ├─ pre-commit
│  │  │  ├─ pre-commit.sample
│  │  │  ├─ pre-merge-commit.sample
│  │  │  ├─ pre-push
│  │  │  ├─ pre-push.sample
│  │  │  ├─ pre-rebase
│  │  │  ├─ pre-rebase.sample
│  │  │  ├─ pre-receive
│  │  │  ├─ pre-receive.sample
│  │  │  ├─ prepare-commit-msg
│  │  │  ├─ prepare-commit-msg.sample
│  │  │  ├─ push-to-checkout
│  │  │  ├─ push-to-checkout.sample
│  │  │  ├─ sendemail-validate
│  │  │  ├─ sendemail-validate.sample
│  │  │  ├─ update
│  │  │  └─ update.sample
│  │  ├─ index
│  │  ├─ info
│  │  │  └─ exclude
│  │  ├─ logs
│  │  │  ├─ HEAD
│  │  │  └─ refs
│  │  │     └─ heads
│  │  │        └─ master
│  │  ├─ objects
│  │  │  ├─ 14
│  │  │  │  └─ 919c0515b598fd258246be1ddfe598b5e47056
│  │  │  ├─ 1b
│  │  │  │  └─ 622fd8b6d082f336562d19915fe95891b00e89
│  │  │  ├─ 21
│  │  │  │  └─ 4388fe43cdfd7ce1c29cd3e401541ded620dba
│  │  │  ├─ 24
│  │  │  │  └─ 0acf47af142f37a7b9b81d6de05058e2afdf14
│  │  │  ├─ 3e
│  │  │  │  └─ 5a13962197105f2078d2a224cc57dfa09b4893
│  │  │  ├─ 3f
│  │  │  │  └─ a28070de24f2055171ca2e20543881cb7fdf1c
│  │  │  ├─ 40
│  │  │  │  └─ 3adbc1e527906a4aa59558cd582c20bcd1d738
│  │  │  ├─ 4a
│  │  │  │  └─ afc5f6ed86fe6dff8d4b6be59290cbdeb61656
│  │  │  ├─ 57
│  │  │  │  └─ 6b9809116131402662fd7174ac478052218c99
│  │  │  ├─ 5d
│  │  │  │  └─ 4b3b7c9704c9c4ee1bb182035051988373acf2
│  │  │  ├─ 64
│  │  │  │  └─ 3aefb67882e1e97408502ae510fb3e0d20210b
│  │  │  ├─ 65
│  │  │  │  ├─ 10c6a45035b6573151ff6196e4bdea78deb75d
│  │  │  │  └─ 9607daa329e1a2c850ffa76cdcf3151cace807
│  │  │  ├─ 67
│  │  │  │  └─ 38d8416c3d77453a596884f2d02d8480bbeb2d
│  │  │  ├─ 69
│  │  │  │  └─ 093ca554de68667f42727bda8a37fc91806b38
│  │  │  ├─ 74
│  │  │  │  └─ 6f8c7022eb6f9fc65bafcfe3dae9a53628020c
│  │  │  ├─ 91
│  │  │  │  └─ 0e297e0f53483455d2aa432887c3b7975d6c11
│  │  │  ├─ 92
│  │  │  │  └─ 4624515c356231d01060e82a207c50fdaed7c2
│  │  │  ├─ 99
│  │  │  │  └─ bf960e214e73e5513e054ac34c331b6d4b1a46
│  │  │  ├─ a3
│  │  │  │  └─ 95a1f86f47699521a7794a3e18b6f8e3fe342d
│  │  │  ├─ b2
│  │  │  │  └─ c8940893973b64fe3e2d13f822dca8cfd9c720
│  │  │  ├─ df
│  │  │  │  └─ 36fcfb72584e00488330b560ebcf34a41c64c2
│  │  │  ├─ e8
│  │  │  │  └─ d96d7a7049d1ddda2073b5bed757935fc35fbc
│  │  │  ├─ e9
│  │  │  │  └─ 558405fdcc02f12d757acb308e02937a7444f1
│  │  │  ├─ f3
│  │  │  │  └─ d2503fc2a44b5053b0837ebea6e87a2d339a43
│  │  │  ├─ fb
│  │  │  │  └─ d2adb37d6a55da58d290121c2d087d7a3dd7df
│  │  │  ├─ info
│  │  │  └─ pack
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ master
│  │     └─ tags
│  ├─ babel.config.js
│  ├─ dockerfile
│  ├─ jsconfig.json
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  ├─ favicon.ico
│  │  └─ index.html
│  ├─ README.md
│  ├─ src
│  │  ├─ App.vue
│  │  ├─ assets
│  │  │  └─ logo.png
│  │  ├─ components
│  │  │  ├─ FeedbackFormDialog.vue
│  │  │  └─ RatingCard.vue
│  │  ├─ main.js
│  │  ├─ router
│  │  │  └─ index.js
│  │  ├─ services
│  │  │  └─ api.js
│  │  └─ views
│  │     ├─ HomeView.vue
│  │     └─ ThankYouView.vue
│  └─ vue.config.js
└─ README.md

```