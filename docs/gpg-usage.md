# GPG Usage

Documentation of GnuPG usage

---

## Table of contents

- [Installation](#installation)
- [Generating a GPG key](#generating-a-gpg-key)
- [Telling Git about your signing key](#telling-git-about-your-signing-key)

---

## Installation

Download and install the GPG command line tools.

- arch: `gnupg`

---

## Generating a GPG key

1. Generate a GPG key pair

    ```bash
    gpg --full-generate-key
    ```

2. At the prompt, specify the kind of key you want, or press `Enter` to accept the default.

3. At the prompt, specify the key size you want, or press `Enter` to accept the default.

4. Enter the length of time the key should be valid. Press `Enter` to specify the default selection, indicating that the key doesn't expire. Unless you require an expiration date, we recommend accepting this default.

5. Verify that your selections are correct.

6. Enter your user ID information.

7. Type a secure passphrase.

8. Use the this command below to list the long form of the GPG keys for which you have both a public and private key. A private key is required for signing commits or tags.

    ```bash
    gpg --list-secret-keys --keyid-format=long
    ```

9. From the list of GPG keys, copy the long form of the GPG key ID you'd like to use. In this example, the GPG key ID is `3AA5C34371567BD2`:

    ```bash
    $ gpg --list-secret-keys --keyid-format=long
    /Users/hubot/.gnupg/secring.gpg
    ------------------------------------
    sec   4096R/3AA5C34371567BD2 2016-03-10 [expires: 2017-03-10]
    uid                          Hubot <hubot@example.com>
    ssb   4096R/4BB6D45482678BE3 2016-03-10
    ```

10. Paste the text below, substituting in the GPG key ID you'd like to use. In this example, the GPG key ID is `3AA5C34371567BD2`:

    ```bash
    gpg --armor --export 3AA5C34371567BD2
    ```

11. Copy your GPG key, beginning with `-----BEGIN PGP PUBLIC KEY BLOCK-----` and ending with `-----END PGP PUBLIC KEY BLOCK-----`.

---

## Telling Git about your signing key

If you're using a GPG key that matches your committer identity and your verified email address associated with your account on GitHub.com, then you can begin signing commits and signing tags.

1. If you have previously configured Git to use a different key format when signing with `--gpg-sign`, unset this configuration so the default format of `openpgp` will be used.

    ```bash
    git config --global --unset gpg.format
    ```

2. Use the this command to list the long form of the GPG keys for which you have both a public and private key. A private key is required for signing commits or tags.

    ```bash
    gpg --list-secret-keys --keyid-format=long
    ```

3. From the list of GPG keys, copy the long form of the GPG key ID you'd like to use. In this example, the GPG key ID is `3AA5C34371567BD2`:

    ```bash
    $ gpg --list-secret-keys --keyid-format=long
    /Users/hubot/.gnupg/secring.gpg
    ------------------------------------
    sec   4096R/3AA5C34371567BD2 2016-03-10 [expires: 2017-03-10]
    uid                          Hubot <hubot@example.com>
    ssb   4096R/4BB6D45482678BE3 2016-03-10
    ```

4. To set your primary GPG signing key in Git, paste the text below, substituting in the GPG primary key ID you'd like to use. In this example, the GPG key ID is `3AA5C34371567BD2`:

    ```bash
    git config --global user.signingkey 3AA5C34371567BD2
    ```

5. Optionally, to configure Git to sign all commits by default, enter the following command:

    ```bash
    git config --global commit.gpgsign true
    ```

---
