# BlackDuckDataChallenge
This projects aims to help people understand the dependencies of a open source project easier.

## Insights found so far:

1. Top 5 Version used by most projects
```
 "<QuerySet [{'name': '5.1.1', 'num_projects': 2}, {'name': 'Additional "
 "Versions', 'num_projects': 2}, {'name': 'UDK2010.SR1.UP1', 'num_projects': "
 "1}, {'name': 'freebsd4_snap_20040419', 'num_projects': 1}, {'name': "
 "'2.14.0', 'num_projects': 1}]>"
 ```

2. Top 5 License used by most projects
 ```
 "<QuerySet [{'id': 45, 'num_projects': 34}, {'id': 3, 'num_projects': 16}, "
 "{'id': 11, 'num_projects': 14}, {'id': 34, 'num_projects': 14}, {'id': -1, "
 "'num_projects': 10}]>"
 ```


3. Top 5 Projects with Highest number of Distinct Properties
 ```
 "<QuerySet [{'id': '317aad06-7ed0-4744-a578-d3e0a9657ed1', 'num_dws': 36, "
 "'num_dns': 36, 'num_so': 1}, {'id': '3186e8de-1fa1-4bc4-8f76-3fcdebbcea1d', "
 "'num_dws': 32, 'num_dns': 31, 'num_so': 5}, {'id': "
 "'3dec9166-bd9d-45d3-acae-9c78adb1a684', 'num_dws': 21, 'num_dns': 21, "
 "'num_so': 18}, {'id': '3f503880-3a3e-4c78-9d1c-01fa18f26e9b', 'num_dws': 25, "
 "'num_dns': 24, 'num_so': 7}, {'id': '8af515ed-25f9-47ea-922b-3b95bfc3aff5', "
 "'num_dws': 26, 'num_dns': 25, 'num_so': 3}]>"
 ```

4. Top 5 Projects with Highest number of License
 ```
 "<QuerySet [{'id': '2ff38a7c-238b-487f-af9b-64a2ec81d81c', 'num_license': "
 "30}, {'id': 'ca691cd3-5ded-46df-935d-2691bbf3c28d', 'num_license': 8}, "
 "{'id': '09212528-db03-4fa1-8aa1-993a848d557c', 'num_license': 5}, {'id': "
 "'9c16dba1-4a5e-40e5-a53c-86749221ac82', 'num_license': 5}, {'id': "
 "'679734a7-af20-465e-8c13-8339259c039e', 'num_license': 4}]>"
 ```

5. Version and the number of projects that use it
 ```
 "<QuerySet [{'version_id': '5.1.1', 'num_project': 2}, {'version_id': "
 "'Additional Versions', 'num_project': 2}, {'version_id': 'UDK2010.SR1.UP1', "
 "'num_project': 1}, {'version_id': '2.14.0', 'num_project': 1}, "
 "{'version_id': '2.5.11', 'num_project': 1}, {'version_id': '10.10.1', "
 "'num_project': 1}, {'version_id': '0.2.0', 'num_project': 1}, {'version_id': "
 "'2.8.0-fuse-01-13', 'num_project': 1}, {'version_id': "
 "'0.37.8-Snap-2014-02-22', 'num_project': 1}, {'version_id': "
 "'hotfix-2014-11-21', 'num_project': 1}, {'version_id': '0.0.1', "
 "'num_project': 1}, {'version_id': 'V.2.6.4', 'num_project': 1}, "
 "{'version_id': 'aura-framework-0.0.388', 'num_project': 1}, {'version_id': "
 "'1.3.4.1', 'num_project': 1}, {'version_id': '3.13.2', 'num_project': 1}, "
 "{'version_id': 'freebsd4_snap_20040419', 'num_project': 1}, {'version_id': "
 "'3.1.0', 'num_project': 1}, {'version_id': '2.7.0.redhat-610394', "
 "'num_project': 1}, {'version_id': 'bsdi3_snap_20010925', 'num_project': 1}, "
 "{'version_id': 'v2.1.9', 'num_project': 1}, '...(remaining elements "
 "truncated)...']>"
 ```

6. License_id and the number of projects that use it
 ```
 "<QuerySet [{'id': 45, 'num_project': 34}, {'id': 3, 'num_project': 16}, "
 "{'id': 11, 'num_project': 14}, {'id': 34, 'num_project': 14}, {'id': 30, "
 "'num_project': 10}, {'id': -1, 'num_project': 10}, {'id': 22, 'num_project': "
 "3}, {'id': 36, 'num_project': 3}, {'id': 12, 'num_project': 2}, {'id': 389, "
 "'num_project': 2}, {'id': 137, 'num_project': 2}, {'id': 15, 'num_project': "
 "2}, {'id': 31, 'num_project': 2}, {'id': 35, 'num_project': 2}, {'id': 77, "
 "'num_project': 2}, {'id': 177, 'num_project': 2}, {'id': 1450, "
 "'num_project': 2}, {'id': 21, 'num_project': 1}, {'id': 364, 'num_project': "
 "1}, {'id': 29, 'num_project': 1}, '...(remaining elements truncated)...']>"
 ```
 
 ### You can download the [Report.txt](https://github.com/Paul-Kijtapart/BlackDuckDataChallenge/blob/master/server/report.txt) file in Server folder
