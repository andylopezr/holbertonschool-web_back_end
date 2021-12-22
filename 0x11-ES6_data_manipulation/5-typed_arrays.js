export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw new Error('Position outside range');
  }
  const a = new ArrayBuffer(length);
  const view = new DataView(a);
  view.setUint8(position, value);
  return view;
}