"""The launcher offers the temporal upscalers (FSR 4 included); spatial upscaling stays out of it."""
import sys
import unittest

from paths import ROOT
sys.path.insert(0, str(ROOT / 'launcher'))
import gow3_launcher_win as launcher


class UpscalerSettingsTest(unittest.TestCase):
    def test_choices_have_fsr4_and_no_spatial_upscaler(self):
        self.assertEqual([value for value, _text in launcher.UPSCALERS], ['fsr4', 'fsr411', 'fsr3', 'taa', 'off'])

    def test_fsr4_asset_list_covers_both_tiers(self):
        files = launcher.fsr4_files()
        self.assertIn('fsr4_model_v07_i8_quality_2160_pass12.spv', files)
        self.assertIn('fsr4_model_v07_i8_quality_1080_pre.spv', files)

    def test_removed_controls_do_not_supply_defaults_to_save(self):
        for key in ('fsr1', 'sharpen', 'sharpness', 'rcas', 'rcas_strength'):
            self.assertNotIn(key, launcher.INI_DEFAULTS)


if __name__ == '__main__':
    unittest.main()
