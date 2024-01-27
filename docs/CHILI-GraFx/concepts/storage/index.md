# Understanding Storage Calculation

This document outlines how your media assets, such as pictures, consume storage space in CHILI GraFx.

## 1. **Uploading Media Assets**

When you upload an asset, it occupies a certain amount of storage space. This space is primarily determined by the file size of the asset. For example, a 1 MB picture will initially take up 1 MB of storage space in your account.

## 2. **The Role of Preview Data**

For optimal performance, our application automatically creates preview data when you upload a media asset. These files are essential for the application to function correctly and efficiently over the web. They allow faster loading times and smoother access to your media, but they also require additional storage space. The size of these files varies depending on the original file but is a necessary part of the storage calculation.

## 3. **Backup Storage**

Data security is paramount for us ([ISO 27001](https://www.chili-publish.com/trust/)). Therefore, CHILI GraFx creates backups of your uploaded media assets, fonts and Smart Templates. These backups are essential to protect your data against accidental loss or corruption. However, like preview files, backups also take up additional storage space. We ensure that your data is safe and readily available whenever you need it, but this safety feature increases the total storage requirement.

## 4. **Total Storage Calculation**

The total storage space you see on your dashboard is not just the sum of the file sizes of your uploaded media. It is, in fact, a multiple of this size. This total includes:

- The original media asset size (e.g., your pictures)
- The font assets
- The Smart Templates
- The storage required for preview files
- The storage required for backups

## Scenario

Below is an example of a scenario where you have Document (Smart Templates), Assets and Fonts. Each have their respective size.

When backed up, we calculate the exact amount of data for the backup. Depending on your scenario, this might be more or less in real life due to snapshots. CHILI GraFx only calculates 100% of the data size.

Preview data, necessary for the system to work performant, is not backed up. In case a backup needs to be recovered, preview data will be recreated by the CHILI GraFx engine.

In the scenario below: **282 MB** will be reported in your storage overview.

| Type of Data  | Size   | Backup Size   | Total |
| ----------- 	| -----: | -----: | --: |
| Documents     | 0.5 GB  | 0.5 GB  | 1 GB |
| Assets        | 100 GB | 100 GB | 200 GB |
| Fonts         | 0.2 GB   | 0.2 GB   | 0.4 GB |
| Preview data  | 10 GB  | n.a. | 10 GB |
| Total  		| **110.7 GB**  | **100.7 GB** | **211.4 GB** |

## Conclusion

Understanding how storage is calculated helps you manage your account effectively. It's important to remember that the total storage usage includes not just your uploaded files but also the additional space required for preview files, fonts, templates and backups, ensuring both performance and data safety.