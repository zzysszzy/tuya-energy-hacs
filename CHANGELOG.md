# Changelog

## [1.0.0] - 2025-07-30

### About This Release

This release is based on the official Home Assistant Tuya integration with enhanced energy monitoring capabilities.

**Original Code Attribution:**

- Original Tuya Integration: Home Assistant Team
- License: Apache License 2.0
- Source: https://github.com/home-assistant/core/tree/dev/homeassistant/components/tuya

### Added

- Complete Tuya integration with enhanced energy monitoring
- Support for all Tuya device types (switches, lights, climate, sensors, etc.)
- Energy monitoring with cumulative and incremental reporting modes
- Device-level energy reporting configuration
- State restoration for energy sensors
- Diagnostic attributes for troubleshooting
- Real-time MQTT device status updates
- Multi-platform support (sensors, binary sensors, switches, lights, climate, covers, fans, etc.)
- Auto-discovery and setup
- Cloud-based device communication
- Comprehensive device support including:
  - Energy monitors and smart plugs
  - Lighting (bulbs, switches, dimmers)
  - Climate (thermostats, heaters, air conditioners)
  - Security (cameras, sensors, alarms)
  - Appliances (fans, humidifiers, vacuums)
  - And all other Tuya-compatible devices

### Features

- **Enhanced Energy Monitoring**: Real-time power, current, voltage, and energy consumption tracking
- **Flexible Energy Reporting**: Support for both cumulative and incremental energy reporting modes
- **Device Configuration**: Per-device energy reporting mode configuration
- **State Persistence**: Automatic state restoration for energy sensors
- **Diagnostic Information**: Detailed attributes for troubleshooting and monitoring
- **Real-time Updates**: MQTT-based real-time device status updates
- **Comprehensive Device Support**: All Tuya device types and categories

### Technical Improvements

- Based on official Tuya integration with energy monitoring enhancements
- Improved error handling and logging
- Enhanced device discovery and management
- Better integration with Home Assistant device registry
- Optimized performance and reliability

### Breaking Changes

- This is a complete rewrite based on the official Tuya integration
- Domain changed from `tuya_energy` to maintain compatibility
- Enhanced energy monitoring capabilities while preserving all original Tuya functionality
