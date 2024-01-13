"""LK ICS.2 integration."""

import asyncio
from datetime import timedelta
import logging
from typing import Any, Dict

from aiohttp import ClientConnectionError
from async_timeout import timeout

from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    ATTR_NAME,
    CONF_HOST,
    CONF_NAME,
)
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.helpers.typing import HomeAssistantType

from .const import (
    DOMAIN,
    TIMEOUT,
)

PLATFORMS = [SENSOR_DOMAIN]
SCAN_INTERVAL = timedelta(seconds=60)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: Dict) -> bool:
  """Set up the LK ICS.2 component."""
  hass.data.setdefault(DOMAIN, {})
  return True


async def async_setup_entry(hass: HomeAssistantType, entry: ConfigEntry):
  return True

async def async_unload_entry(hass, config_entry):
  """Unload a config entry."""
  await asyncio.wait(
      [
          hass.config_entries.async_forward_entry_unload(config_entry, component)
          for component in PLATFORMS
      ]
  )
  hass.data[DOMAIN].pop(config_entry.entry_id)
  if not hass.data[DOMAIN]:
    hass.data.pop(DOMAIN)
  return True

