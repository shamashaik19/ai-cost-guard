import ServiceCard from "./ServiceCard";

const services = ["EC2", "S3", "RDS", "Lambda"];

export default function Dashboard() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">
        AWS Cost Guard Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        {services.map(s => (
          <ServiceCard key={s} name={s} />
        ))}
      </div>
    </div>
  );
}
