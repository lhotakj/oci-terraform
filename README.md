# OCI terraform

A basic Terraform action running Terraform code on Oracle Cloud Infrastructure (OCI)

## oci-terraform/init

Downloads and initializes your terraform working directory. It also safely injects your credentials -- this is done by
overriding
`provider "oci" {}` section. Due to a limitation in th provider credentials cannot be used as variable, but embedded
inside the file.

| Inputs                 | Type     | Default value | Description                                                                                  |
|------------------------|----------|---------------|----------------------------------------------------------------------------------------------|
| `private_key`          | `string` |               | Mandatory. Content of the private file of your OCI Token                                     |
| `fingerprint`          | `string` |               | Mandatory. Fingerprint of your OCI TOKEN                                                     |
| `private_key_password` | `string` |               | Optional. Password of the private file of your OCI Token                                     |
| `version`              | `string` | `latest`      | Optional. value defining target version of Terraform, if not set it uses the latest version. |
| `context`              | `string` | `.`           | Optional. Path where is located Terraform code, by default it takes the current folder.      |

### Known limitations

- Make sure do checkout first, so the folder defined in `context` variable contains your terraform code

⚠️ The development is still ongoing!

