#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/24 13:36
@Author  : Caps
@File    : 查找webapps
"""

import os
import re
import shutil

st = '1. 3DExplore' \
     '2. ENOVIAEnterpriseChangeManagement' \
     '3. ENOVIACollaborativeTasksFoundation' \
     '4. ENOVIAIPClassificationFoundation' \
     '5. ENOVIAProjectManagementFoundation' \
     '6. DELMIAManufacturingModelingFoundation' \
     '7. DataModelCustomizationFoundation' \
     '8. ENOVIADocumentManagement' \
     '9. ENOVIAX-CADDesignFoundation' \
     '10. ENOVIAIntegrationExchangeFramework' \
     '11. ENOVIACollaborationforMicrosoftServer' \
     '12. DELMIAConnectorforApriso' \
     '13. ENOVIAUnifiedX-CADDesignManagement' \
     '14. CATIASystemsDesigner' \
     '15. ENOVIACopyandArtworkFoundation' \
     '16. ENOVIATraceableRequirementsManagementFoundation' \
     '17. CATIASystemsEmbeddedElectronics' \
     '18. CATIASystemsTraceability' \
     '19. ENOVIAEngineeringBOMManagementFoundation' \
     '20. ENOVIAEnterpriseAVLManagement' \
     '21. ENOVIAEBOMAVLManagement' \
     '22. ENOVIAVariantManagementFoundation' \
     '23. ENOVIAConfiguredBOMManagementFoundation' \
     '24. ENOVIAManufacturingBOMManagementFoundation' \
     '25. ENOVIABOMandDMRFoundation' \
     '26. ENOVIAPDFRenderingMonitorService' \
     '27. ENOVIAMarketRegistrationFoundation' \
     '28. ENOVIADeviceIdentificationFoundation' \
     '29. ENOVIAAdverseEventReportingFoundation' \
     '30. ENOVIAProductSpecificationsFoundation' \
     '31. ENOVIAIPProtectionandExportControlManagement' \
     '32. ENOVIAUnitBOMManagementFoundation' \
     '33. LiveCollaborationServer' \
     '34. ENOVIAMaterialsComplianceCentralSupplierPortalClient' \
     '35. ENOVIAMaterialsComplianceFoundation' \
     '36. ENOVIABOMMaterialsCompliancyFoundation' \
     '37. ENOVIAMaterialsComplianceReportingFoundation' \
     '38. DELMIAMfgItemsStructurePlanner' \
     '39. DELMIAManufacturingAssetsDefinition' \
     '40. ENOVIAHigh-TechNewPartRequestandDevelopmentOverlay' \
     '41. DELMIAProcessReview' \
     '42. DELMIA3DWorkbook' \
     '43. DELMIA3DLean' \
     '44. CATIAQualityCheckerConfiguration' \
     '45. ENOVIADocumentControlFoundation' \
     '46. ENOVIACAPAandAuditFoundation' \
     '47. ENOVIAComplaintsandNonConformancesFoundation' \
     '48. ENOVIAProjectandDHFManagementFoundation' \
     '49. CATIASystemsReportGeneration' \
     '50. CATIASystemsExperienceValidation' \
     '51. ENOVIASupplierItemManagement' \
     '52. ENOVIASpecificationManagementFoundation' \
    # 需要查找的webapp根路径
webapps_dir = r'E:\3DE R2022x GA'
# 存放找到的webapp路径，如果不存在会创建
copy_dest_path = r'E:\3DE安装教学(基于r2022x)\linux安装\webapps'

# 写入命令
cmdlist = []


def find_file(names, f, root):
    '''
    查找文件
    :param names: 文件列表
    :param f: 当前文件
    :param root: 当前文件夹
    :return:
    '''
    for i, n in enumerate(names):
        if n + '-' in f and 'V6R2022x.Linux64.tar.gz' in f:
            print(f'found {n} in: {os.path.join(root, f)}')
            desc_name = f'{str(i + 1)}.' + f
            shutil.copy(os.path.join(root, f), copy_dest_path + "/" + desc_name)
            cmdlist.append((i + 1, desc_name, n))
            break


# 3. 从命令行中结构化解析参数
if __name__ == '__main__':
    pat = '(\d+\.)'
    st = re.compile(pat).sub('*', st)
    print(st)
    names = [i.strip() for i in st.split('*') if i]
    for i, item in enumerate(names):
        print(i, ' ', item)
