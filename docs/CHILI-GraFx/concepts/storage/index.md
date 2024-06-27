# Understanding Storage Calculation

This document outlines how your assets, such as pictures, consume storage space in CHILI GraFx.

## Dashboard
Your journey in understanding storage starts on the Dashboard of [CHILI GraFx](https://chiligrafx.com). Here, a graph neatly displays the total storage used across all your environments.

You have the option to delve into specific environments using a dropdown selector.

![find environment](find_environment.png)

In each environment, storage usage is broken down into several categories:
- Media assets (images you upload)
- Font assets
- Smart Templates
- Storage for preview files
- Storage for backups

![environment breakdown](env_breakdown.png)

!!! note

    This data is not in real-time and it can take up to two weeks for data changes to be reflected.

## Understanding Storage Dynamics

### Uploading Media Assets
When you upload a media asset, it consumes storage equivalent to its file size. For instance, uploading a 1 MB image will use 1 MB of your storage quota.

### Uploading Font Assets
Similar to Media Assets, when you upload a font asset it occupies a certain amount of storage space. GraFx Fonts only allows you to upload only one copy of font style per font family. GraFx Publisher allows you to upload multiple copies.

### Smart Templates
Creating a new smart template (GraFx Studio Templates, GraFx Studio Projects, or GraFx Publisher Documents) also uses storage. These files are typically small, under 400 KB, but larger and more complex templates will occupy more space.

### Preview Data
Our system automatically generates preview data for media assets and smart templates to enhance performance. These previews ensure quicker load times and smoother access but do require extra storage. The size varies based on the original file.

### Backup Storage
Data security is paramount for us ([ISO 27001](https://www.chili-publish.com/trust/)). Therefore, CHILI GraFx creates backups of your uploaded media assets, fonts and Smart Templates. These backups are essential to protect your data against accidental loss or corruption. However, like preview files, backups also take up additional storage space.

## Scenario
Consider this example: you have Documents (Smart Templates), Assets, and Fonts with their respective sizes. 

Backups are exact duplicates of your data, and their size might vary in real-world scenarios. CHILI GraFx always considers 100% of the data size for backup calculations. Note that preview data, crucial for system performance, is not included in backups. In a recovery situation, the CHILI GraFx engine will regenerate this data.

In this example, **282 MB** is the total storage displayed in your overview.

| Type of Data  | Size   | Backup Size   | Total |
| ----------- 	| -----: | -----: | --: |
| Documents     | 0.5 GB  | 0.5 GB  | 1 GB |
| Assets        | 100 GB | 100 GB | 200 GB |
| Fonts         | 0.2 GB   | 0.2 GB   | 0.4 GB |
| Preview data  | 10 GB  | n.a. | 10 GB |
| Total  		| **110.7 GB**  | **100.7 GB** | **211.4 GB** |

## Conclusion
Understanding how storage is calculated helps you manage your account effectively. The total storage footprint encompasses not only your uploaded files but also the additional space needed for previews, fonts, templates, and backups, balancing performance with data security.

If you're integrating CHILI GraFx into your workflow, developing a strategy for regular cleanup of old assets and templates is advisable for optimal storage management.
