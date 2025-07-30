#!/usr/bin/env python3
"""
Test script for Tuya API connection
"""

import asyncio
import sys
import os

# Add the custom component to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'custom_components'))

from tuya_sharing import LoginControl

async def test_tuya_connection():
    """Test Tuya API connection."""
    try:
        # Initialize LoginControl
        login_control = LoginControl()
        
        # Test QR code generation
        print("Testing Tuya API connection...")
        
        # You can test with a sample user code
        user_code = "test_user_code"
        
        # This will help identify if the issue is with the API or the integration
        print(f"LoginControl initialized: {login_control}")
        print("If you see this message, the import is working correctly.")
        
    except Exception as e:
        print(f"Error testing Tuya connection: {e}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_tuya_connection()) 