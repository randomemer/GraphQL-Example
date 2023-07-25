import modules.core as core

# Import all the routes to setup

# Frontend Routes
import routes.index
import routes.app
import routes.login
import routes.register

# API Routes
import routes.users
import routes.todos

if __name__ == "__main__":
    core.app.run(debug=True, port=4000)