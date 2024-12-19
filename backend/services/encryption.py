# TODO: Implement real encryption/decryption logic.
# This is a placeholder.

def encrypt(content: str, key: str) -> bytes:
    # Mock encryption: Just encode for now.
    return content.encode("utf-8")

def decrypt(content: bytes, key: str) -> str:
    # Mock decryption: Just decode for now.
    return content.decode("utf-8")
