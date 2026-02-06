"""Debug page to test GitHub connection."""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

st.title("🔍 GitHub Connection Debug")

st.write("### Testing GitHub Connection...")

try:
    from github import Github
    
    # Check if secrets exist
    st.write("**1. Checking secrets...**")
    if "GITHUB_TOKEN" in st.secrets:
        token = st.secrets["GITHUB_TOKEN"]
        st.success(f"✅ Token found (length: {len(token)})")
        st.code(f"Token starts with: {token[:10]}...")
    else:
        st.error("❌ GITHUB_TOKEN not found in secrets")
        st.stop()
    
    if "REPO_NAME" in st.secrets:
        repo_name = st.secrets["REPO_NAME"]
        st.success(f"✅ Repo name: {repo_name}")
    else:
        st.error("❌ REPO_NAME not found in secrets")
        st.stop()
    
    # Test GitHub connection
    st.write("**2. Testing GitHub API connection...**")
    g = Github(token)
    user = g.get_user()
    st.success(f"✅ Authenticated as: {user.login}")
    
    # Test repository access
    st.write("**3. Testing repository access...**")
    repo = g.get_repo(repo_name)
    st.success(f"✅ Repository found: {repo.full_name}")
    st.info(f"Private: {repo.private}")
    
    # Test permissions
    st.write("**4. Testing permissions...**")
    perms = repo.permissions
    st.write(f"- Admin: {perms.admin}")
    st.write(f"- Push: {perms.push}")
    st.write(f"- Pull: {perms.pull}")
    
    if perms.push:
        st.success("✅ Has PUSH permission - should be able to create files!")
    else:
        st.error("❌ No PUSH permission - this is the problem!")
    
    # Test creating a file
    st.write("**5. Testing file creation...**")
    if st.button("🧪 Test Create File"):
        try:
            test_content = "This is a test file"
            test_path = "test-debug.txt"
            
            # Try to create the file
            repo.create_file(
                test_path,
                "Test commit from debug",
                test_content,
                branch="main"
            )
            st.success("✅ File creation successful! Your setup is working!")
            st.info("You can delete 'test-debug.txt' from your repo now.")
            
        except Exception as e:
            st.error(f"❌ File creation failed: {str(e)}")
            st.write("**Error details:**")
            st.code(str(e))
    
except Exception as e:
    st.error(f"❌ Error: {str(e)}")
    st.write("**Full error:**")
    st.code(str(e))
    
    import traceback
    st.write("**Traceback:**")
    st.code(traceback.format_exc())

st.markdown("---")
st.write("**Your current secrets (for verification):**")
st.code(f"""
GITHUB_TOKEN = "{st.secrets.get('GITHUB_TOKEN', 'NOT SET')[:20]}..."
REPO_NAME = "{st.secrets.get('REPO_NAME', 'NOT SET')}"
""")
