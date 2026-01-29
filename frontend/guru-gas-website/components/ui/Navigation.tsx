import Link from "next/link";
import { Button } from "@/components/ui/button";
export default function Navbar(){
    return(
        <nav className="flex justify-between gap-4 items-center p-4 border-b bg-rgb(248, 240, 231)">
            <div className="flex gap-4">
                <Link href="/" className="hover: underline">
                <Button>Home</Button>
                </Link>
                <Link href="/products" className="hover: underline">
                <Button>Products</Button>
                </Link>
                <Link href="/cart" className="hover: underline flex items-right">
                <Button>Cart</Button>
                </Link>
            </div>

        </nav>
    )
}