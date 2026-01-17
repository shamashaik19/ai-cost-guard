export default function ServiceCard({ name }) {
  return (
    <div className="bg-slate-800 rounded-xl p-6 shadow-lg border border-slate-700">
      <h2 className="text-xl font-semibold">{name}</h2>
      <p className="text-green-400 mt-2">Active</p>
    </div>
  );
}
