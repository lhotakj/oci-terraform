# OCI terraform
A basic Terraform action running Terraform code on Oracle Cloud Infrastructure (OCI)


| Inputs                 | Type     | Default value | Description                                                                                  |
|------------------------|----------|---------------|----------------------------------------------------------------------------------------------|
| `private_key`          | `string` |               | Mandatory. Content of the private file of your OCI Token                                     |
| `fingerprint`          | `string` |               | Mandatory. Fingerprint of your OCI TOKEN                                                     |
| `private_key_password` | `string` |               | Optional. Password of the private file of your OCI Token                                     |
| `version`              | `string` | `latest`      | Optional. value defining target version of Terraform, if not set it uses the latest version. |
| `context`              | `string` | `.`           | Optional. Path where is located Terraform code, by default it takes the current folder.      |

⚠️ The developement is still ongoing

