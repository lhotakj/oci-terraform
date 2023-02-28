# OCI terraform

A basic Terraform action running Terraform code on Oracle Cloud Infrastructure (OCI)

## oci-terraform/init

This action has to be called very first, it doesn't do just the installation of terraform working directory and prepares secrets, but configures [Oracle Command Line Interface (CLI)](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm).

The inputs are all what the Oracle Cloud Infrastructure [expects](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm)*, plus some specific variables    

| Inputs                  | Type     | Default value | Description                                                                                                                                                                               |
|-------------------------|----------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `private_key`*          | `string` |               | Mandatory. Content of the private file of your OCI Token, PEM format                                                                                                                      |
| `private_key_password`* | `string` |               | Optional. In case you used a password for you OCI Token.                                                                                                                                  |
| `fingerprint`*          | `string` |               | Mandatory. Fingerprint of your OCI TOKEN, [instructions](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#four) how to get it                                    |
| `user_ocid`*            | `string` |               | Mandatory. User's OCID, see the [instructions](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#five) where to find it                                           |
| `tenancy_ocid`*         | `string` |               | Mandatory. Tenancy's OCID, see the [instructions](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#five) where to find it                                        |
| `compartment_ocid`*     | `string` |               | Mandatory. Compartment OCID, see the [instructions](https://docs.oracle.com/en-us/iaas/Content/GSG/Tasks/contactingsupport_topic-Finding_the_OCID_of_a_Compartment.htm) where to find it  |
| `region`*               | `string` |               | Mandatory. The code of the region you want to deploy your architecture, refer to the list of [supported regions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm) |
| `tf_state_uri`          | `string` |               | Mandatory. The URL to the `terraform.tfstate` file, see [documentation](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/terraformUsingObjectStore.htm)                             | 
| `terraform_version`     | `string` | `latest`      | Optional. Value defining target version of Terraform, if not set it uses the latest version.                                                                                              |
| `ssh_public_key`        | `string` |               | Mandatory. Ssh key to be copied to the instances into `authorized_keys` so you can connect there.                                                                                         |
| `ssh_private_key`       | `string` |               | Mandatory only if you run Ansible. In order to run ansible you need to provide a valid SSH key pair so Ansible can properly connect on the host and execute your playbook                 |
| `context`               | `string` | `.`           | Optional. Path where is located Terraform code, by default it takes the current folder.                                                                                                   |

### Example
```
jobs:
  build-docker-images:
    name: Terraform Oracle
    runs-on: ubuntu-latest

    env:
      TF_VAR_tenancy_ocid: ocid1.tenancy.oc1..aaaaaaaaXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      TF_VAR_user_ocid: ocid1.user.oc1..aaaaaaaasXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      TF_VAR_compartment_ocid: ocid1.tenancy.oc1..aaaaaaaaXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      TF_VAR_region: eu-frankfurt-1
      
      # these to be created as secrets!
      TF_VAR_PRIVATE_KEY: -----BEGIN RSA PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED\nDEK-Info: AES-128-CBC,87BA0BA9A5A7E3BC07011D1612474A0F\n/7jwUpXQYWztjj9Yoqlpwov8RwiZBMr8auJy6dhQXtnukYHsVSE7c2qwa3k3YrjH\nXXXXXXXXXXXXXXXXXXXXX'
      TF_VAR_PRIVATE_KEY_PASSWORD: 'mysupersecretprivatekey
      TF_VAR_FINGERPRINT: '59:45:c7:e8:eb:c1:bb:7e:5a:a0:55:e9:f2:14:86:5b9'
      TF_VAR_SSH_PUBLIC_KEY: 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
      TF_VAR_SSH_PRIVATE_KEY: '-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA3BxCSUrCB5GhTO64qQ\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
      TF_VAR_STATE_URI: 'https://objectstorage.<region>.oraclecloud.com/<my-access-uri>'
      
    steps:
      - name: "Checkout"
        uses: "actions/checkout@master"
      - name: "Terraform init ..."
        uses: "lhotakj/oci-terraform/init@main"
        with:
          tenancy_ocid: ${{ env.TF_VAR_tenancy_ocid }}
          user_ocid: ${{ env.TF_VAR_user_ocid }}
          compartment_ocid: ${{ env.TF_VAR_compartment_ocid }}
          region: ${{ env.TF_VAR_region }}
          private_key: ${{ secrets.TF_VAR_PRIVATE_KEY }}
          private_key_password: ${{ secrets.TF_VAR_PRIVATE_KEY_PASSWORD }}
          fingerprint: ${{ secrets.TF_VAR_FINGERPRINT }}
          ssh_public_key: ${{ secrets.TF_VAR_SSH_PUBLIC_KEY }}
          ssh_private_key: ${{ secrets.TF_VAR_SSH_PRIVATE_KEY }}
          tf_state_uri: ${{ env.TF_VAR_STATE_URI }}
          context: terraform
```

### Known limitations

- Make sure do checkout first, so the folder defined in `context` variable contains your terraform code

⚠️ The development is still ongoing!

