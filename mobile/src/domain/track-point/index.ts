// mobile/src/domain/track-point/index.ts
// Public exports fuer den TrackPointV1-Domainkern.
export {
  TRACK_POINT_SOURCE_VALUES,
  TRACK_POINT_QUALITY_VALUES,
  TrackPointV1Schema,
  TrackPointValidationError,
  validateTrackPoint,
  toFiniteOrNull,
  type TrackPointV1,
  type TrackPointSource,
  type TrackPointQuality,
} from './track-point';
export {
  SerializationError,
  serializeTrackPoint,
  deserializeTrackPoint,
  serializePoints,
  deserializePoints,
} from './serialization';
