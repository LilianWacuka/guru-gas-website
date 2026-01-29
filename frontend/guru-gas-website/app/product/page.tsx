"use client";
import Image from "next/image";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardDescription,} from "@/components/ui/card";

export default function ProductPage() {
  return (
    <div className="container px-4 py-10 grid grid-cols-1 md:grid-cols-3 gap-6">
      <Card className="rounded-xl shadow-sm overflow-hidden">
        <div className="flex justify-center bg-gray-50 p-4">
          <Image
            src="https://img.freepik.com/premium-vector/red-gas-cylinder-white-background_627700-63.jpg"
            alt="gas cylinder"
            width={250}
            height={320}
            className="object-contain"
          />
        </div>
        <CardContent className="flex flex-col gap-4 p-6">
          <h1 className="text-xl font-semibold">Gas Name</h1>
          <span className="text-2xl font-bold text-green-600">
            Amount: 3,000
          </span>

          <div className="flex items-center gap-2">
            <label className="font-medium">Weight:</label>
            <select className="border border-gray-300 rounded-md p-2 flex-1">
              <option>10kg</option>
              <option>15kg</option>
              <option>20kg</option>
            </select>
          </div>

          <div className="flex items-center gap-2">
            <label className="font-medium">Quantity:</label>
            <Input
              type="number"
              defaultValue={1}
              min={1}
              className="w-20"
            />
          </div>

          <CardDescription>
            <p className="text-sm text-muted-foreground leading-relaxed">
              This is a high-quality gas cylinder with a weight of 10kg.
              Suitable for both domestic and industrial use.
            </p>
          </CardDescription>

          <div className="flex gap-4 pt-2">
            <Button className="flex-1 bg-blue-600 hover:bg-blue-700">
              Add to Cart
            </Button>
            <Button variant="outline" className="flex-1">
              Buy Now
            </Button>
          </div>
        </CardContent>

      </Card>
    </div>
  );
}
