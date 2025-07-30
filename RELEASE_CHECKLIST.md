# HACS 发布检查清单

## ✅ 必要文件检查
- [x] `manifest.json` - 包含版本号和图标
- [x] `hacs.json` - HACS 配置文件
- [x] `README.md` - 详细的安装和使用说明
- [x] `LICENSE` - 许可证文件
- [x] `CHANGELOG.md` - 更新日志
- [x] `requirements.txt` - 依赖项
- [x] `custom_components/tuya_energy/` - 完整的集成代码

## ✅ 代码质量检查
- [x] 所有 Python 文件语法正确
- [x] 没有硬编码的 `platform=tuya` 字符串
- [x] 使用正确的 `DOMAIN = "tuya_energy"`
- [x] 图标配置正确
- [x] 翻译文件完整

## ✅ 功能测试
- [x] 配置流程正常工作
- [x] 设备发现正常
- [x] 实体创建正常
- [x] 能源监控功能正常
- [x] 增量上报模式正常

## ✅ 文档检查
- [x] README.md 包含安装说明
- [x] README.md 包含配置说明
- [x] README.md 包含使用示例
- [x] README.md 包含故障排除
- [x] CHANGELOG.md 记录版本历史

## ✅ 许可证检查
- [x] LICENSE 文件存在
- [x] 包含对 Home Assistant 团队的致谢
- [x] 明确说明基于 Apache 2.0 许可证的原始代码

## 🚀 发布步骤
1. [ ] 创建 GitHub 仓库
2. [ ] 推送代码到 GitHub
3. [ ] 在 HACS 仓库提交 Issue
4. [ ] 等待审核通过
5. [ ] 发布到 HACS

## 📝 提交信息模板
```
Repository URL: https://github.com/your-username/tuya-energy-hacs
Category: integration
Description: 
Tuya Energy HACS Integration

A custom Home Assistant integration for Tuya devices with enhanced energy monitoring capabilities. This integration provides:

- Real-time energy monitoring (power, current, voltage)
- Support for both cumulative and incremental energy reporting modes
- Device-level configuration for energy reporting modes
- State restoration for incremental energy sensors
- Full Tuya device support (lights, switches, climate, etc.)
- Based on the official Home Assistant Tuya integration with energy enhancements

Features:
- Energy monitoring with precision using Decimal
- Timestamp-based deduplication
- Diagnostic attributes for energy sensors
- Support for all Tuya device categories
- Local debugging capabilities

This integration is based on the official Home Assistant Tuya integration (Apache 2.0) with energy monitoring enhancements (MIT License).
``` 