# GPG Usage

Documentation of GnuPG usage

---

## Table of contents

- [Basic Command](#basic-commands)
- [Git GPG Sign](#git-gpg-sign)

---

## Basic Commands

1. Generate a Key Pair

    ```sh
    gpg --gen-key # or --full-generate-key
    ```

2. Encrypt a File for a Recipient

    ```sh
    gpg --encrypt --recipient recipient@example.com file.txt
    ```

3. Decrypt a File

    ```sh
    gpg --decrypt file.txt.gpg
    ```

4. Sign a File:

    ```sh
    gpg --sign file.txt
    ```

5. Verify a Signature

    ```sh
    gpg --verify file.txt.sig
    ```

6. Export a Key

    ```sh
    gpg --export --armor recipient@example.com --output public_key.asc
    gpg --export-secret-keys --armor --output private_key.asc
    ```

7. Import a Public Key

    ```sh
    gpg --import public_key.asc
    ```

8. List Keys

    ```sh
    gpg --list-keys
    ```

9. Edit a key

    ```sh
    gpg --edit-key YOUR_KEY_ID
    ```

---

## Git GPG Sign

Git GPG signing allows you to sign your commits and tags to ensure their authenticity. By signing your commits with GPG, others can verify that the commits were made by you and haven't been tampered with.
On github.com, you need to use your verified email address associated with your account.

1. If you have previously configured Git to use a different key format when signing with `--gpg-sign`, unset this configuration so the default format of `openpgp` will be used.

    ```sh
    git config --global --unset gpg.format
    ```

2. Configure Git to Use Your GPG Key.

    ```sh
    git config --global user.signingkey YOUR_KEY_ID
    ```

3. Enable Commit Signing

    - Automatic:

        ```sh
        git config --global commit.gpgsign true
        ```

    - Manually:

        ```sh
        git commit -S -m "Your commit message"
        ```

---
