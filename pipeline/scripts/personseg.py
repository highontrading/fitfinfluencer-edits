# Person cut-out mask (mediapipe selfie multiclass), temporally smoothed. Used to put text *behind* the speaker.
import os, numpy as np, cv2
import mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
MODEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models', 'selfie_multiclass.tflite')

class PersonSeg:
    def __init__(self, work_w=540):
        opt = vision.ImageSegmenterOptions(base_options=BaseOptions(model_asset_path=MODEL), output_confidence_masks=True,
                                           running_mode=vision.RunningMode.IMAGE)
        self.seg = vision.ImageSegmenter.create_from_options(opt)
        self.ww = work_w; self.prev = None; self.prev_f = None
    def mask(self, rgb, f=None):
        """float32 HxW in [0,1]: 1 = person. rgb is HxWx3 uint8 (RGB)."""
        H, W = rgb.shape[:2]; wh = int(round(H * self.ww / W))
        small = np.ascontiguousarray(cv2.resize(rgb, (self.ww, wh), interpolation=cv2.INTER_AREA))
        r = self.seg.segment(mp.Image(image_format=mp.ImageFormat.SRGB, data=small))
        m = 1.0 - r.confidence_masks[0].numpy_view().reshape(wh, self.ww).astype(np.float32)
        if self.prev is not None and f is not None and self.prev_f == f - 1:
            m = 0.6 * m + 0.4 * self.prev          # light temporal smoothing (only across consecutive frames)
        self.prev, self.prev_f = m, f
        m = cv2.GaussianBlur(m, (0, 0), 1.2)
        m = np.clip((m - 0.35) / 0.4, 0, 1)        # firm edges, soft falloff
        return cv2.resize(m, (W, H), interpolation=cv2.INTER_LINEAR)
