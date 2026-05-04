#!/usr/bin/env python
"""
Database Initialization Script
Run this once before starting the app for the first time.
Usage:
    python init_db.py              # Just create tables
    python init_db.py --demo       # Create tables + demo user
"""

import sys
from app import app, db, User, Prediction


def init_database():
    """Create all database tables"""
    with app.app_context():
        print("=" * 50)
        print("  BigMart Sales - Database Initialization")
        print("=" * 50)

        print("\n🔄 Creating database tables...")
        db.create_all()
        print("✅ Tables created successfully!")

        # Show current data count
        user_count = User.query.count()
        pred_count = Prediction.query.count()
        print(f"\n📊 Current Data:")
        print(f"   Users       : {user_count}")
        print(f"   Predictions : {pred_count}")

        print("\n✅ Database is ready!")
        print("   Run: python app.py to start the server\n")


def create_demo_user():
    """Create a demo user for testing"""
    with app.app_context():
        print("\n🔄 Creating demo user...")

        if User.query.filter_by(email='demo@bigmart.com').first():
            print("⚠️  Demo user already exists — skipping.")
            return

        user = User(name='Demo User', email='demo@bigmart.com')
        user.set_password('demo1234')
        db.session.add(user)
        db.session.commit()

        print("✅ Demo user created!")
        print("   Email    : demo@bigmart.com")
        print("   Password : demo1234")


if __name__ == '__main__':
    init_database()

    if len(sys.argv) > 1 and sys.argv[1] == '--demo':
        create_demo_user()

    print("=" * 50)
    print("🎉 Setup complete! Ready to run.")
    print("=" * 50)
